import random


def generate_random_integer(min_value, max_value):
    """
    Generate Random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_opertaor():
    """
        Generate a random arithmetic operator.
    """
    return random.choice(['+', '-', '*'])


def generate_expression(num1, num2, operator):
    """
            Determine result of the arithmetic expression
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return problem, result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_opertaor()

        problem, answer = generate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # To Handle invalid input
        try:

        user_answer = int(input("Your answer: "))
        except ValueError:
        print("Invalid input. Enter a valid integer input ")
        user_answer = 0

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
