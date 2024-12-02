import re
import os

def get_input_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_numbers_from_string(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def is_sequence_valid(numbers):
    """
    Check if a sequence of numbers satisfies the condition:
    consecutive differences are within [-3, -1] or [1, 3].
    """
    return all([(numbers[i] - numbers[i+1]) in [1, 2, 3] or
                (numbers[i] - numbers[i+1]) in [-1, -2, -3] 
                for i in range(len(numbers) - 1)])

def solve_puzzle(input_text):
    """
    Parse the input text and calculate the counters based on specific rules
    """
    part1 = 0
    part2 = 0

    for line in input_text.split('\n'):
        if line.strip():
            numbers = get_numbers_from_string(line)
            
            # Part 1: Check if the full sequence is valid.
            if is_sequence_valid(numbers):
                part1 += 1
            
            # Part 2: Check validity of sequences with one number removed.
            for i in range(len(numbers)):
                modified_sequence = numbers[:i] + numbers[i+1:]
                if is_sequence_valid(modified_sequence):
                    part2 += 1
                    break

    return part1, part2

if __name__ == "__main__":
    try:
        input_text = read_input(get_input_path('input.txt'))
        result = solve_puzzle(input_text)
        print(result)
    except FileNotFoundError:
        print("Error: Input file not found")
    except ValueError as e:
        print(f"Error parsing input: {e}")
