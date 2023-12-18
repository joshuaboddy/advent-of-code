import pandas as pd
import itertools


def find_empty_rows_in_grid(grid):
    
    empty_rows = []
    
    for row in grid.iterrows():
        if (row[1] == ".").all():
            empty_rows.append(row[0])
            
    return empty_rows

    
def find_empty_columns_in_grid(grid):
    
    empty_columns = []
    
    for idx, col in enumerate(grid.columns):
        if (grid[col] == ".").all():
            empty_columns.append(idx)
            
    return empty_columns
        

def get_galaxy_coords_from_grid(grid, empty_rows, empty_columns, empty_space_multiplier):
    
    galaxies = []
    
    for idx, col in enumerate(grid.columns):
        for row in grid.iterrows():
            if grid[col][row[0]] == "#":
                
                empty_column_multiplier = sum([col > empty_column for empty_column in empty_columns])
                empty_row_multiplier = sum([row[0] > empty_row for empty_row in empty_rows]) 
                
                galaxies.append((col + (empty_space_multiplier - 1) * empty_column_multiplier, 
                               row[0] + (empty_space_multiplier - 1) * empty_row_multiplier))
                
    return galaxies


def get_sum_of_lengths_between_galaxy_pairs(galaxies):
    
    galaxy_pairs = itertools.combinations(galaxies, 2)
    sum_of_lengths = 0
    
    for galaxy_pair in galaxy_pairs:
        x_diff = abs(galaxy_pair[0][0] - galaxy_pair[1][0])
        y_diff = abs(galaxy_pair[0][1] - galaxy_pair[1][1])
        steps = x_diff + y_diff
        sum_of_lengths += steps
    
    return sum_of_lengths


def main(grid, empty_space_multiplier):
    
    empty_rows = find_empty_rows_in_grid(grid)
    empty_columns = find_empty_columns_in_grid(grid)
    
    galaxies = get_galaxy_coords_from_grid(grid, empty_rows, empty_columns, empty_space_multiplier)
    
    return get_sum_of_lengths_between_galaxy_pairs(galaxies)


f = open("input.txt", "r")

lines = f.readlines()

grid = pd.DataFrame([[char for char in line.strip()] for line in lines])

print(main(grid, 2))
print(main(grid, 1e6))
