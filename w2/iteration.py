# Find numbers dividable by 6
def exercise_1():
    for x in range(0, 100):
        if x % 6 == 0:
            print(x)


def exercise_2():
    largest = -1
    smallest = -1
    total = 0
    counter = 0

    while total < 50:
        value = -1

        while value < 1 or value > 10:
            value = int(input(f'Enter a valid number between 1 and 10:\n'))

        if value > largest or largest == -1:
            largest = value

        if value < smallest or smallest == -1:
            smallest = value

        counter += 1
        total += value

    average = total / counter

    print(f"Total: {total} Counter: {counter}")
    print(f"Largest: {largest} Smallest: {smallest}")
    print(f"Average: {average}")



