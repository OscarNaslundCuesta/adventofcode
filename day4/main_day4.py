with open("day4/input_day4.txt", "r") as input:
    lines = input.readlines()

list = []
list1 = []
list2 = []
count = 0

for line in lines:
    list = line.strip().split(',')
    
    firstHalf = list[0]
    secondHalf = list[1]

    list1 = firstHalf.split('-')
    int1 = list1[0]
    int2 = list1[1]

    list2 = secondHalf.split('-')
    int3 = list2[0]
    int4 = list2[1]

    if int(int1) >= int(int3) and int(int1) <= int(int4) and int(int2) <= int(int4) and int(int2) >= int(int3) or int(int3) >= int(int1) and int(int3) <= int(int2) and int(int4) <= int(int2) and int(int4) >= int(int1):
        count += 1

print(count)