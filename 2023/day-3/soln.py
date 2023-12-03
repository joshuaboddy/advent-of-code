def adjacent_check(row_idx, col_idx, grid):
    moves = [-1, 0, 1]

    for x_move in moves:
        x = row_idx + x_move
        
        if 0 <= x < len(grid):
            for y_move in moves:
                y = col_idx + y_move
                
                if 0 <= y < len(grid[x]):
                    adjacent = grid[x][y]
                    
                    if adjacent != '.' and not adjacent.isdigit():
                        return True
                    
    return False
                     

def get_coords_with_adjacent_symbols_and_get_stars(grid):
    
    has_adjacent = []
    stars = []
    for row_idx, line in enumerate(grid):
        for col_idx, char in enumerate(line):
            if char.isdigit() and adjacent_check(row_idx, col_idx, grid):
                     has_adjacent.append((row_idx, col_idx))
                
            if char == "*":
                stars.append((row_idx, col_idx))
                
    return has_adjacent, stars
            
            
def get_number_if_has_adjacent_symbols(has_adjacent, grid):
    
    coord_has_been_visited = []
    one_coord_and_number = {}

    for row_and_col in has_adjacent:
        row = row_and_col[0]
        col = row_and_col[1]
        
        if (row, col) not in coord_has_been_visited:
            
            line = grid[row]
            
            number = line[col]
            coord_has_been_visited.append((row, col))
            
            go_left = 1
            while (col - go_left) < len(line) and line[col - go_left].isdigit():
                number = line[col - go_left] + number
                coord_has_been_visited.append((row, col - go_left))
                go_left += 1
                
                
            go_right = 1
            while (col + go_right) < len(line) and line[col + go_right].isdigit():
                number += line[col + go_right]
                coord_has_been_visited.append((row, col + go_right))
                go_right += 1
                
            one_coord_and_number[(row, col)] = int(number)
                
    return one_coord_and_number


def get_gear_ratio_sum(stars, one_coord_and_number):
    
    moves = [-1, 0, 1]
    gear_ratio_sum = 0
    
    for star in stars:
        number_of_adjacent_numbers = 0
        gear_ratio = 1
        
        for x_move in moves:
            for y_move in moves:
                x, y = star[0] + x_move, star[1] + y_move
                
                if (x, y) in one_coord_and_number:
                    number_of_adjacent_numbers += 1
                    gear_ratio *= one_coord_and_number[(x, y)]
        
        if number_of_adjacent_numbers == 2:
            gear_ratio_sum += gear_ratio
            
    return gear_ratio_sum


f = open("input.txt", "r")
grid = [line.strip() for line in f.readlines()]

has_adjacent, stars = get_coords_with_adjacent_symbols_and_get_stars(grid)
one_coord_and_number = get_number_if_has_adjacent_symbols(has_adjacent, grid)
gear_ratio_sum = get_gear_ratio_sum(stars, one_coord_and_number)

print(sum(one_coord_and_number.values()))
print(gear_ratio_sum)
        
    