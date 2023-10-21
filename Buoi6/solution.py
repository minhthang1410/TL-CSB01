import random

print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores.")
score = 0

for i in range(3):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    phep_toan = random.randint(1, 3)
    if phep_toan == 1:
        result = a + b
        user_result = int(input(f"{a} + {b} = "))
        if result == user_result:
            score += 1
            print("Correct !!!")
        else:
            print("Incorrect !!!")
    elif phep_toan == 2:
        result = a - b
        user_result = int(input(f"{a} - {b} = "))
        if result == user_result:
            score += 1
            print("Correct !!!")
        else:
            print("Incorrect !!!")
    elif phep_toan == 3:
        result = a * b
        user_result = int(input(f"{a} * {b} = "))
        if result == user_result:
            score += 1
            print("Correct !!!")
        else:
            print("Incorrect !!!")

print("== GAME OVER ==")
print(f"Your total score is {score}")
