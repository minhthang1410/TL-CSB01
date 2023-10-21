import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))
print(f"Mảng ban đầu: {numbers}")

# so_chan = []

# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         so_chan.append(numbers[i])

# print(f"Mảng số chẵn: {so_chan}")

# numbers_greater_than_50 = []

# for i in range(len(numbers)):
#     if numbers[i] >= 50:
#         numbers_greater_than_50.append(numbers[i])

# print(f"Mảng các số lớn hơn 50: {numbers_greater_than_50}")
# print(f"Tỉ lệ: {len(numbers_greater_than_50) / len(numbers)}")

# Tìm max
# max = numbers[0]

# for i in range(len(numbers)):
#     if numbers[i] > max:
#         max = numbers[i]

# print(f"Số lớn nhất trong mảng là: {max}")

# Tìm min
min = numbers[0]

for i in range(len(numbers)):
    if numbers[i] < min:
        min = numbers[i]

print(f"Số nhỏ nhất trong mảng là: {min}")

print(f"Max của mảng ban đầu là: {max(numbers)}")
