import random

# Questions and answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Jupiter", "B. Saturn", "C. Mars", "D. Venus"],
        "correct_answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Harper Lee"],
        "correct_answer": "D"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "correct_answer": "B"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "correct_answer": "B"
    }
]


def play_kbc():
    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions. Each correct answer will earn you points.")
    print("Let's begin!\n")

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q['correct_answer']:
            score += 1
            print("Correct! Well done!")
        else:
            print(f"Sorry, that's incorrect. The correct answer was {q['correct_answer']}.")
        print()

    print(f"Game Over! Your final score is: {score} out of {len(questions)}")

    if score == len(questions):
        print("Congratulations! You've won the grand prize!")
    elif score >= len(questions) // 2:
        print("Well played! You've won a consolation prize.")
    else:
        print("Better luck next time!")


# MADE BY RISHABH GHOSH 
play_kbc()
