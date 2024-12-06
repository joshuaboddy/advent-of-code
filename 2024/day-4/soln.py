import os

def get_input_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def parse_input_to_grid(input_text):
    grid = {}
    for line_index, line in enumerate(input_text.split()):
        for char_index, char in enumerate(line):
            grid[(char_index, line_index)] = char
    return grid

def check_direction(grid, start_coord, dx, dy):
    return ''.join(grid.get((start_coord[0] + i*dx, start_coord[1] + i*dy), "") for i in range(len("XMAS"))) == "XMAS"

def part_1(grid, starting_coord):
    directions = [
        (1, 0),   # right
        (-1, 0),  # left
        (0, -1),  # up
        (0, 1),   # down
        (1, 1),   # diagonal down-right
        (-1, 1),  # diagonal down-left
        (1, -1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]
    return sum(check_direction(grid, starting_coord, dx, dy) for dx, dy in directions)

def check_diagonal(grid, start_coord, dx, dy):
    pattern = ''.join(grid.get((start_coord[0] + i*dx, start_coord[1] + i*dy), "") for i in [-1,0,1])
    return pattern in ["MAS", "SAM"]

def part_2(grid, starting_coord):
    diagonals = [
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal up-right
    ]
    return all(check_diagonal(grid, starting_coord, dx, dy) for dx, dy in diagonals)

if __name__ == "__main__":
    try:
        input_text = read_input(get_input_path('input.txt'))
        grid = parse_input_to_grid(input_text)

        print(sum(part_1(grid, coord) for coord in grid))
        print(sum(part_2(grid, coord) for coord in grid))
            
    except FileNotFoundError:
        print("Error: Input file not found")
    except ValueError as e:
        print(f"Error parsing input: {e}")
