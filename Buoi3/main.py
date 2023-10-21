import math
# Tính nghiệm phương trình bậc 2
a = int(input("Nhập tham số a: "))
b = int(input("Nhập tham số b: "))
c = int(input("Nhập tham số c: "))

delta = (b * b) - (4 * a * c)

if (delta < 0):
    print("Phương trình vô nghiệm")
elif (delta == 0):
    print(f"Phương trình có nghiệm kép là {(-1 * b) / (2 * a)}")
else:
    x1 = ((-1 * b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(delta)) / (2 * a)
    print("Phương trình có 2 nghiệm phân biệt")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
