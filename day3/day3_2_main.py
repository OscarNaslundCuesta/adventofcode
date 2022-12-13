with open("day3/input_day3.txt", "r") as input:
    strings = input.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
badges = ''
sum = 0
temp_strings3 = []

for string in strings:
    temp_strings3.append(string.strip())

    temp_duplicates = ''
    if len(temp_strings3) == 3:
        duplicate_found = False
        for i in temp_strings3[0]:
            if i in temp_strings3[1] and i in temp_strings3[2] and duplicate_found == False:
                duplicate_found = True
                badges += i
        temp_strings3 = []

for i in badges:
    add = alphabet.index(i)+1
    sum += add

print(sum)