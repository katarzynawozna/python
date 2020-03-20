import random

def random_numbers():
    numbers = []
    numbers = [str(random.randint(1, 10)) for x in range(3)]
    return ' '.join(numbers)

file = open("LICZBY.txt", "w+", encoding="utf-8")

for line in range(100):
    file.write(random_numbers() + "\n")

file.close()

with open("LICZBY.txt") as f:
    numbers = [number.rstrip() for number in f]


def if_triangle(numbers):
    threes = []
    for x in range(len(numbers)):
        three = numbers[x].split()
        three = [int(x) for x in three]
        threes.append(three)

    indexes = []
    
    for x in range(len(numbers)):
        if numbers[x][0] + numbers[x][1] < numbers[x][2]:
            indexes.append(x+1)
        elif numbers[x][0] + numbers[x][2] < numbers[x][1]:
            indexes.append(x+1)
        elif numbers[x][2] + numbers[x][1] < numbers[x][0]:
            indexes.append(x+1)
    
    if len(indexes) == 0:
        return "Nie można zbudować trójkątów z żadnych z tych liczb"
    else:
        index = ', '.join(str(x) for x in indexes)
        return f"Trójkąt można zbudować z boków podanych w liniach: {index} "

print(if_triangle(numbers))