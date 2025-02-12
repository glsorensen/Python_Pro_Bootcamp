#Range

for number in range(1, 10):
    print(number)


for number in range(1, 10, 2):
    print(number)

total = 0

for number in range(0,101):
    total += number
print(total)

total = sum(range(1, 101))
print(total)