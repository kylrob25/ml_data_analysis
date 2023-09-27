values = []

i = 1
while i < 3:
    values[i] = int(input('Enter number'))
    i = i + 1

total = 0

for x in values:
    total += x

print("Total: " + total)

