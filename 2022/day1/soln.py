f = open('input.txt')
raw = f.readlines()
f.close()

part = 2
max_elf_scores = [0] * (1 if part == 1 else 3)
current_elf_score = 0
for line in raw:
    if line != '\n':
        current_elf_score += int(line.strip())
    else:
        if any([score < current_elf_score for score in max_elf_scores]):
            max_elf_scores = sorted(max_elf_scores, reverse=True)
            max_elf_scores.pop()
            max_elf_scores.append(current_elf_score)
        current_elf_score = 0
        
print(sum(max_elf_scores))

        