import os
import re

def get_input_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_numbers_from_string(s):
    return [int(x) for x in re.findall(r'\d+', s)]

def parse_input(input_text):
    pages_order = {}
    updates = []
    
    for line in input_text.split():
        numbers = get_numbers_from_string(line)
        if "|" in line:
            before_page, after_page = numbers
            pages_order.setdefault(before_page, []).append(after_page)
        elif line:
            updates.append(numbers)
            
    return pages_order, updates

def find_incorrect_updates(pages_order, updates):
    part_1_total = 0
    incorrects = []
    
    for update in updates:
        reversed_update = update[::-1]
        
        for idx, num in enumerate(reversed_update):
            preceding_pages = reversed_update[idx + 1:]
            if not preceding_pages: 
                part_1_total += update[len(update) // 2] 
                
            if num in pages_order and any(page in preceding_pages for page in pages_order[num]):
                incorrects.append(update)
                break
                
    return part_1_total, incorrects

def topological_sort(graph, page, visited, temp_visited, sorted_pages):
    if page in temp_visited or page in visited:
        return
        
    temp_visited.add(page)
    for next_page in graph.get(page, []):
        topological_sort(graph, next_page, visited, temp_visited, sorted_pages)
    temp_visited.remove(page)
    visited.add(page)
    sorted_pages.append(page)

def build_graph(incorrect, pages_order):
    return {num: [p for p in pages_order.get(num, []) if p in incorrect] for num in incorrect}

def process_incorrect_updates(incorrects, pages_order):
    total_middle = 0
    
    for incorrect in incorrects:
        graph = build_graph(incorrect, pages_order)
        sorted_pages = []
        visited = set()
        temp_visited = set()
        
        for page in incorrect:
            if page not in visited:
                topological_sort(graph, page, visited, temp_visited, sorted_pages)
                
        correct_order = sorted_pages[::-1]
        total_middle += correct_order[len(correct_order) // 2]
        
    return total_middle

def main():
    try:
        input_text = read_input(get_input_path('input.txt'))
        pages_order, updates = parse_input(input_text)
        part_1_total, incorrects = find_incorrect_updates(pages_order, updates)
        part_2_total = process_incorrect_updates(incorrects, pages_order)
        
        print(part_1_total)
        print(part_2_total)
        
    except FileNotFoundError:
        print("Error: Input file not found")
    except ValueError as e:
        print(f"Error parsing input: {e}")

if __name__ == "__main__":
    main()
