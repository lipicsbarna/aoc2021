## coordinates_str = input_file as an ugly, huge multiline string

from shapely.geometry import LineString, Point

coordinates_str_list = coordinates_str.split("\n")

coordinates = [
    (   
        tuple((int(x) for x in (row.split(" -> ")[0]).split(","))), 
        tuple((int(x) for x in (row.split(" -> ")[1]).split(",")))
    ) 
    for row in coordinates_str_list
]

# Only horizontal and vertical
hori_verti = [c for c in coordinates if (c[0][0] == c[1][0]) or (c[0][1] == c[1][1])]
lines = [LineString(x) for x in hori_verti]

def calculate_intersections(lines: list[LineString], intersections = [] ) -> list[Point]:
    
    if len(lines) == 0:
        return intersections
    else:
        popp = lines.pop()
        points = [ popp.intersection(other_point) for other_point in lines if popp.intersects(other_point) ]
        intersections.append(points)
    
        return calculate_intersections(lines, intersections)
    
intersections = calculate_intersections(lines)
flat_intersections = [item for sublist in intersections for item in sublist]

print(set([g.type for g in flat_intersections if g.type != 'Point']))
## {'LineString'}

# Round 1 - Can't do diagonal 
def pointify_linestring(ls: LineString) -> list[Point]:
    if ls.xy[0][0] == ls.xy[0][1]:
        fix_coord = int(ls.xy[0][0])
        fix_idx = 0
        moving_idx = 1
    elif ls.xy[1][0] == ls.xy[1][1]:
        fix_coord = int(ls.xy[1][1])
        fix_idx = 1
        moving_idx = 0
    else:
        print(list(ls.coords))
        
    start = int(min(ls.xy[moving_idx]))
    end   = int(max(ls.xy[moving_idx])) + 1
 
    points = []

    for p in range(start, end):
        coords = [0,0]
        coords[fix_idx] = fix_coord
        coords[moving_idx] = p
        points.append(Point(*coords))
    
    return points

linestring_points = [pointify_linestring(l) for l in [g for g in flat_intersections if g.type != 'Point']]
flat_linestring_points = [item for sublist in linestring_points for item in sublist]

all_points = [g for g in flat_intersections if g.type == 'Point'] + (flat_linestring_points)

# Result1
print(len(set([p.wkt for p in all_points])))

# Round 2 - WARNING - My code doesn't give the appropriate answer for the puzzle - still don't get why.
# I used a dumb matrix walking shit instead of this nice one
def pointify_diagonal_linestring(ls: LineString) -> list[Point]:
    points = []
    i = 0
    moving_coord = ls.coords[0]
    while moving_coord != ls.coords[1]:
        _rounded = [int(round(c)) for c in moving_coord]
        points.append(Point(*_rounded))
        i += sqrt(2)
        moving_coord = ls.interpolate(i).coords[0]
    return points


def pointify_all_linestring(ls: LineString) -> list[Point]:
    try:
        return pointify_linestring(ls)
    except:
        return pointify_diagonal_linestring(ls)


lines = [LineString(x) for x in coordinates]
intersections = calculate_intersections(lines)
flat_intersections = [item for sublist in intersections for item in sublist]

linestring_points = [pointify_all_linestring(l) for l in [g for g in flat_intersections if g.type != 'Point']]
flat_linestring_points = [item for sublist in linestring_points for item in sublist]

all_points = [g for g in flat_intersections if g.type == 'Point'] + (flat_linestring_points)
print(len(set([p.wkt for p in all_points])))


