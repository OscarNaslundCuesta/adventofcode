with open("day2/input_day2.txt", "r") as input:
    games = input.readlines()

points = 0

#def play():
#    pre_result = game.strip()
#    result = pre_result.split(" ")
#    calc(result[0], result[1])

def calc(a, b):
    global points
    
    if b == 'X':
        points += 0
        if a == 'A':
            points += 3
        elif a == 'B':
            points += 1
        elif a == 'C':
            points += 2

    elif b == 'Y':
        points += 3
        if a == 'A':
            points += 1
        elif a == 'B':
            points += 2
        elif a == 'C':
            points += 3

    elif b == 'Z':
        points += 6
        if a == 'A':
            points += 2
        elif a == 'B':
            points += 3
        elif a == 'C':
            points += 1

    return(points)
    
for game in games:
    pre_result = game.strip()
    result = pre_result.split(" ")
    points = calc(result[0], result[1])

print(points)