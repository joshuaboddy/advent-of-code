import re
import os
import math

def get_input_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_numbers_from_string(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def get_sumproduct_of_mul_from_string(s):
    matches = re.findall(r'mul\(\d+,\d+\)', s)
    return sum(math.prod(get_numbers_from_string(match)) for match in matches)

if __name__ == "__main__":
    try:
        input_text = read_input(get_input_path('input.txt'))

        part1 = get_sumproduct_of_mul_from_string(input_text)

        part2 = 0
        do_strings = input_text.split("do()")
        for do_string in do_strings:
            do_string_with_dont_removed = do_string.split("don't()")[0]
            part2 += get_sumproduct_of_mul_from_string(do_string_with_dont_removed)

        print(part1, part2)
        

    except FileNotFoundError:
        print("Error: Input file not found")
    except ValueError as e:
        print(f"Error parsing input: {e}")
