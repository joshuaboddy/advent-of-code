import re

def read_input(file_path):
    """Read and return contents of file at given path."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_numbers_from_string(s):
    """Extract and return list of integers from string."""
    return [int(x) for x in re.findall(r'\d+', s)]

def part1(left_list, right_list):
    """Calculate total absolute difference between sorted pairs."""
    total_difference = 0
    for left, right in zip(left_list, right_list):
        total_difference += abs(right - left)
    return total_difference

def part2(left_list, right_list):
    """Calculate sum of products of matching numbers."""
    product_sum = 0
    for left in left_list:
        product_sum += left * right_list.count(left)
    return product_sum

def parse_input(input_text):
    """Parse input text and return sorted lists of left and right numbers."""
    numbers_left = []
    numbers_right = []
    for line in input_text.split('\n'):
        if line:
            left_and_right = get_numbers_from_string(line)
            numbers_left.append(left_and_right[0])
            numbers_right.append(left_and_right[1])

    numbers_left.sort()
    numbers_right.sort()
    return numbers_left, numbers_right

if __name__ == "__main__":
    try:
        input_text = read_input('2024/day-1/input.txt')
        numbers_left, numbers_right = parse_input(input_text)
        
        print(part1(numbers_left, numbers_right))
        print(part2(numbers_left, numbers_right))
    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"Error: {e}")
