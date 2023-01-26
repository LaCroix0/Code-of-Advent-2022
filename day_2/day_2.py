rules = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

rules_draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

rules_win = {
    'C': 'X',
    'A': 'Y',
    'B': 'Z'
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def match(opponent_move, your_move):
    for k in rules_draw:
        if opponent_move == k and your_move == rules_draw[k]:
            score = 3 + points[your_move]
            return score
    for x in rules:
        if opponent_move == x and your_move == rules[x]:
            score = 0 + points[your_move]
            return score
    else:
        score = 6 + points[your_move]
        return score


def predicted_match(opponent_move, your_move):
    for x in rules_draw:
        if opponent_move == x and your_move == "Y":
            return match(x, rules_draw[x])
    for y in rules:
        if opponent_move == y and your_move == "X":
            return match(y, rules[y])
        elif opponent_move == y and your_move == "Z":
            return match(y, rules_win[y])


total_points = 0
predicted_points = 0

with open('input.txt', 'r') as file:
    for line in file:
        linia = str(line)
        total_points += match(linia[0], linia[2])
        predicted_points += predicted_match(linia[0], linia[2])
file.close()

print(f"Total number of points:", total_points)
print(f"Number of points with predicted outcome:", predicted_points)