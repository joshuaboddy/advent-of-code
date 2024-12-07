import os
import re
import itertools

def get_input_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def extract_numbers(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def apply_operation(lhs, rhs, operators):
    result = lhs
    for i, op in enumerate(operators):
        if op == '*':
            result *= rhs[i + 1]
        elif op == '+':
            result += rhs[i + 1]
        elif op == '||':
            result = int(f'{result}{rhs[i + 1]}')
    return result

def evaluate_equations(input_text, operators):
    
    solved_equation_total = 0

    for line in input_text:
        numbers = extract_numbers(line)
        lhs = numbers[0]
        rhs = numbers[1:]

        combinations = itertools.product(operators, repeat=len(rhs) - 1)

        for combo in combinations:
            result = apply_operation(rhs[0], rhs, combo)
            if result == lhs:
                solved_equation_total += lhs
                break

    return solved_equation_total

if __name__ == "__main__":
    input_text = read_input(get_input_path('input.txt'))
    print(evaluate_equations(input_text, operators = ['*', '+', '||']))
