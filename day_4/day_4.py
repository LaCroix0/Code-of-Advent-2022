

with open('input.txt', 'r') as file:
    inp = file.read().strip()
    sections = inp.split('\n')

total = 0
total_part2 = 0
for sec in sections:
        var1, var2 = sec.split(',')
        var1_start, var1_end = map(int, var1.split('-'))
        var2_start, var2_end = map(int, var2.split('-'))

        if(var1_start <= var2_start and var2_end <= var1_end) \
        or (var2_start <= var1_start and var1_end <= var2_end):
            total += 1

        if set(range(var1_start, var1_end + 1)) & set(range(var2_start, var2_end + 1)):
            total_part2 += 1

print(f"Number of assignments that are fully covered by the second elf:", total)
print(f"Overlapping assignments:", total_part2)