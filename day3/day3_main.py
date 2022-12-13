with open("day3/input_day3.txt", "r") as input:
    strings = input.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
duplicates = ''
sum = 0

for string in strings:
    middle = int(len(string.strip())/2)
    length = int(len(string.strip()))

    firstHalf = str(string[ 0:middle ])
    secondHalf = str(string[ middle:length ])

    temp_duplicates = ''

    for i in firstHalf:
        if i in secondHalf and i not in temp_duplicates:
            temp_duplicates += i
            duplicates += temp_duplicates

for i in duplicates:
    add = alphabet.rfind(i)+1
    sum += add

print(sum)