import random

# List of questions (each question is a dictionary)
questions = [
    {
        "question": "What is the capital of Kenya?",
        "choices": ["A. Nairobi", "B. Mombasa", "C. Kisumu", "D. Nakuru"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "choices": ["A. Python", "B. JavaScript", "C. HTML", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What is 5 + 7?",
        "choices": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "question": "Which one is a loop in Python?",
        "choices": ["A. if", "B. for", "C. def", "D. print"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    }
]

# Shuffle questions randomly
random.shuffle(questions)

score = 0

print("Welcome to the Quiz App!\n")

# Loop through each question
for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    
    # Display choices
    for choice in q["choices"]:
        print(choice)
    
    # Get user input
    user_answer = input("Your answer (A/B/C/D): ").upper()
    
    # Check answer
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")

# Display final score
print(f"Your final score is {score} out of {len(questions)}.")

# Provide feedback
if score == len(questions):
    print("Excellent! Perfect score!")
elif score >= len(questions) // 2:
    print("Good job! You did well.")
else:
    print("Keep practicing! You can improve.")
