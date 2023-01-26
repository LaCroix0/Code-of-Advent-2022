total = 0
with open('input.txt', 'r') as file:
        inp = file.read().strip()

rucksacks = inp.split('\n')

counter = 0
for rs in rucksacks:
    length = len(rs)
    compartment1 = rs[: length // 2]
    compartment2= rs[length // 2:]
    for item in compartment1:
        if item in compartment2:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26
            total += value
            break

i = 0
total_2 = 0
while i < len(rucksacks):
    bag1 = rucksacks[i]
    bag2 = rucksacks[i + 1]
    bag3 = rucksacks[i + 2]
    for item in bag1:
        if item in bag2 and item in bag3:
            value = ord(item) - 96 if item.islower() else ord(item) - 64 + 26
            total_2 += value
            i += 3
            break

print(f"Common score:", total)
print(f"Summed score per groups:", total_2)