f = open('input.txt')
raw = f.readlines()
f.close()

points = {
    "win": 6,
    "draw": 3,
    "lose": 0
    }

# part 1
choices = {
    "A": ("Rock", 1),
    "X": ("Rock", 1),
    "B": ("Paper", 2), 
    "Y": ("Paper", 2),
    "C": ("Scissors", 3),
    "Z": ("Scissors", 3)
    }


total_p2_points = 0
for line in raw:
    line = line.strip()
    p1, p2 = line.split(" ")
    
    if (choices[p1][0] == "Rock" and choices[p2][0] == "Scissors"):
        total_p2_points += choices[p2][1] + points["lose"]
        
    elif (choices[p2][0] == "Rock" and choices[p1][0] == "Scissors"):
        total_p2_points += choices[p2][1] + points["win"]
        
    elif choices[p1][1] > choices[p2][1]:
        total_p2_points += choices[p2][1] + points["lose"]
        
    elif choices[p1][1] < choices[p2][1]:
        total_p2_points += choices[p2][1] + points["win"]
        
    else: 
        total_p2_points += choices[p2][1] + points["draw"]
        
print(total_p2_points)


# part 2
points_and_results = {
    "A": 1,
    "X": "lose",
    "B": 2, 
    "Y": "draw",
    "C": 3,
    "Z": "win"
    }


total_p2_points = 0
for line in raw:
    line = line.strip()
    p1, p2 = line.split(" ")
    
    p1_points = points_and_results[p1]
    result = points_and_results[p2]
    result_points = points[result]
    
    total_p2_points += result_points
    if result == "lose":
        total_p2_points += (p1_points - 1) if p1_points != 1 else 3
    elif result == "win": 
        total_p2_points += p1_points % 3 + 1
    else:
        total_p2_points += p1_points
        
print(total_p2_points)