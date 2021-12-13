# input_str = input_file as always: an ugly, lazy multiline string
import numpy as np
import pandas as pd

coords_str = input_str.split("\n\n")[0]
folds_str = input_str.split("\n\n")[1]

coords = [[ int(c.split(",")[0]), int(c.split(",")[1]) ] for c in coords_str.split("\n")]
folds = [(c.split("=")[0], int(c.split("=")[1]) ) for c in folds_str.replace("fold along ", "").split("\n")]

# Used numbers instead of the strings
x_max = max([c[0] for c in coords])
y_max = max([c[1] for c in coords])
paper = np.zeros((y_max+1, x_max+1))
for c in coords:
    paper[c[1]][c[0]] = 1

def fold_paper(input_paper: np.array, fold_axis_str: str, fold_axis_value: int):
    if fold_axis_str == 'y':
        fold_axis = 0
        not_folded_part = input_paper[0:fold_axis_value, :]
        folded_lonely_part = input_paper[fold_axis_value+1:, :]
        shadow_shape = ((not_folded_part.shape[0] - folded_lonely_part.shape[0]), not_folded_part.shape[1])

    else:
        fold_axis = 1
        not_folded_part = input_paper[:, 0:fold_axis_value]
        folded_lonely_part = input_paper[:, fold_axis_value+1:]
        shadow_shape = (not_folded_part.shape[0], (not_folded_part.shape[1] - folded_lonely_part.shape[1]))

    shadow = np.zeros(shadow_shape)
    folded_not_lonely_anymore = np.concatenate((folded_lonely_part, shadow), fold_axis)
    folded_part = np.flip(folded_not_lonely_anymore, fold_axis)
    folded = not_folded_part + folded_part
    
    return folded

# First
input_paper = paper
for axis, value in folds[0]:
    input_paper = fold_paper(input_paper, axis, value)
    
print(np.sum(first != 0))

# Second
input_paper = paper
for axis, value in folds:
    input_paper = fold_paper(input_paper, axis, value)
    
df = pd.DataFrame(input_paper)

def paper_coloring(val):
    color = 'red' if val > 0 else 'white'
    return 'color: %s' % color

# Did it in Jupyter, it is quite readable
df.style.applymap(_color_red_or_green)

