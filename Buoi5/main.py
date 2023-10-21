import random


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-",])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2

    question = f"What is {num1} {operator} {num2}?"
    return question, answer


def play_game():
    score = 0
    num_questions = 5

    for i in range(num_questions):
        question, answer = generate_question()
        print(f"Question {i+1}: {question}")
        user_answer = float(input("Your answer: "))

        if user_answer == answer:
            score += 1
            print("\nCorrect!\n")
        else:
            print(f"\nWrong! The correct answer is {answer}\n")

        print(f"Game over! Your score is {score}/{num_questions}")


play_game()
