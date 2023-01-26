with open('input.txt', 'r') as file:
    data = file.read().split('\n')

for line in data:
    if line[0] == '$':
        