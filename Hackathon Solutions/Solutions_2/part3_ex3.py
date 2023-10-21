# get user inputs
print('Input the list of numbers.')
print('Enter 0 to finish')

numbers = []
while True:
    num = int(input())
    if num == 0:  # finish input
        break
    numbers.append(num)

print(numbers)
tong = 0
for number in numbers:
    tong += number
print('Sum of all numbers:', tong)
