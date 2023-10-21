# name = input("What your name: ")
# age = float(input("How old are u: "))

# # Đưa giá trị biến vào chuỗi
# # Cách 1
# print(f'My name is {name} ,I\'m {age} yearolds')
# print(len(name))
# Cách 2
# print("My name is {} ,I'm {} yearolds".format(name, age))
# str = "Hello World"
# print(str.lower())
# print(str.upper())

# Kiểu dữ liệu số
# a = float(input("Nhập số a: "))
# b = float(input("Nhập số b: "))
# tong = a + b
# hieu = a - b
# tich = a * b
# thuong = a / b

# print(f'Tổng a và b là {tong}')
# print(f'Hiệu a và b là {hieu}')
# print(f'Tích a và b là {tich}')
# print(f'Thương a và b là {thuong}')

import turtle

# # Nhập vào 3 góc của tam giác
a = int(input("Nhập góc thứ nhất: "))
b = int(input("Nhập góc thứ hai: "))

t = turtle.Turtle()

t.forward(100)
t.left(180)
t.right(a)
t.forward(100)
t.left(180)
t.right(b)
t.forward(100)

turtle.mainloop()
