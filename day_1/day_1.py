total = 0
previous_elf = []
with open('input.txt', 'r') as file:
    for line in file:
        try:
            num = int(line)
            total += num
            # print(f"Number:", num)
        except ValueError:
            previous_elf.append(total)
            total = 0
            # print("-" * 20)
file.close()
previous_elf.sort()
top_elf = previous_elf[-1]
top_3_elfs = sum(previous_elf[-3:])
print("Elf with the most value:", (top_elf))
print("Sum of values for top 3 elfs:", (top_3_elfs))