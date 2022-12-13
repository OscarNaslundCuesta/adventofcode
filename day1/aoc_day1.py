with open("day1/aoc_day1_input.txt", "r") as input:
    lines = input.readlines()

dict = {}
elf_num = 1
sum_cals = 0

for line in lines:
    num = line.strip()
    if num:
        sum_cals += int(num)

    else:
        dict[elf_num]=sum_cals

        elf_num += 1
        sum_cals = 0

max_cals = max(dict.values())
print(max_cals)

dict_sorted = sorted(dict.items(), key = lambda x:x[1], reverse=True)[:3]
print(dict_sorted)

print(69625+69092+72240)