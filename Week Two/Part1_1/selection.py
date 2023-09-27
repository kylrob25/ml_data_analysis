value = -1

while value < 1 or value > 100:
    value = int(input('Please enter a valid number between 1 and 100'))
else:
    even = (value % 2) == 0
    print(even)