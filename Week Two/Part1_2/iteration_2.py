total = 0
additions = 0
values = []

while total < 50:
    value = int(input('Enter a value between 1 and 10\n'))

    if value < 1 or value > 10:
        value = int(input('Enter a valid value between 1 and 10\n'))
    else:
        total += value
        values.append(value)
        additions += 1

largest = values[0]
smallest = values[0]

for value in values:
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value

print(f'Total: {total}\nAdditions: {additions} Largest: {largest} Smallest: {smallest}\nAverage: {total / len(values)}')


