from turtle import *
# Bài 7: Tam giác đặc biệt
canh1 = int(input("Nhập vào một số bất kì: "))
canh2 = int(input("Nhập vào một số bất kì: "))
canh3 = int(input("Nhập vào một số bất kì: "))

if (canh1 < canh2 + canh3) and (canh2 < canh1 + canh3) and (canh3 < canh2 + canh1):
    if (canh1 == canh2 and canh2 == canh3):
        print("The 3 line segments can form an equilateral triangle.")
        forward(canh1)
        left(120)
        forward(canh2)
        left(120)
        forward(canh3)
        mainloop()
    elif (canh1**2 == canh2**2 + canh3**2) or (canh2**2 == canh1**2 + canh3**2) or (canh3**2 == canh2**2 + canh1**2):
        print("The 3 line segments can form a right triangle.")
    else:
        print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")
