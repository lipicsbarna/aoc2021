# crab_positions: np.array = input_file to np.array
import numpy as np

# Round 1
fuel_for_positions = {}
for i in range(min(crab_positions), max(crab_positions)):
    fuel_for_positions.update({i: np.sum(np.abs(i - crab_positions))})
    
min_value = min(fuel_for_positions.values())
print(min_value)

# Round 2
# The given calculation is just (n**2 + n) / 2
fuel_for_crabby_position = {}
for i in range(min(crab_positions), max(crab_positions)):
    used_fuel = np.sum((np.abs(i - crab_positions) ** 2 + np.abs(i - crab_positions)) / 2)
    fuel_for_crabby_position.update({i: used_fuel})
    
min_value = min(fuel_for_crabby_position.values())
print(min_value)
