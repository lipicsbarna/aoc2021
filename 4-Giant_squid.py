### bingo_str = input_file as giant squi..I mean multiline string
import numpy as np

marked_nums = [int(num) for num in bingo_str.split("\n\n")[0].split(',')]

def table_to_matrix(table):
    rows_str = table.replace("  ", " ").split("\n")
    rows = [r.split(' ') for r in rows_str]
    for idx, num in enumerate(rows):
        rows[idx] = [int(element) for element in rows[idx] if element != '']
        
    rows = np.array(rows)
    return rows

bingo_tables = [table_to_matrix(t) for t in bingo_str.split("\n\n")[1:]]

# numpy baby comes to help
marked_np = np.array(marked_nums)

def check_marked_numbers(marked_numbers: np.array, table: np.array) -> tuple(int, int):
    
    blank = np.zeros((5,5), int) + 1
    matches = []
    unmatched = []
    marked_number = 0
    won_score = 0
    is_winner = False
    for counter, marked in enumerate(marked_numbers):
        coord = np.where(table == marked)
        if len(coord[0]) != 0:
            matches.append(coord)
            blank[coord] = 0

    
        if counter >= 4:
            for row in blank:
                if sum(row) == 0:
                    is_winner = True
                    break
                    
            for col in blank.T:
                if sum(col) == 0:
                    is_winner = True
                    break
                    
        if is_winner:
            return (counter, (np.sum(blank * table) * marked))

    return 0


winning_tables = [check_marked_numbers(marked_np, table) for table in bingo_tables]
winning_tables.sort()

# Result
fastest = winning_tables[0]
last = winning_tables[-1]

