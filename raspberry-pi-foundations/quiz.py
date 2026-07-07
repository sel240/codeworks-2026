#Quiz made by RUe Cantor

score = 0

questions = [
    {
        "question": "1. Which of the following was directly caused by Nicol Bolas",
        "options": [
            "A. The Mending",
            "B. Fall of Phyrexia",
            "C. Rise of Phyrexia",
            "D. The Eldrazi existing"
        ],
        "answer": "A"
    },
    {
        "question": "2. Which of these characters are Planeswalkers",
        "options": [
            "A. Spiderman",
            "B. Krenko",
            "C. Bonny Pall",
            "D. Hatsune Miku"
        ],
        "answer": "D"
    },
    {
        "question": "3. Which of these is the name for the color combination red white green",
        "options": [
            "A. Jundt",
            "B. WUBRG",
            "C. Naya",
            "D. Grixxus"
        ],
        "answer": "C"
    }
]

print("====Welcome To The quiz of MTG====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter Your Answer (A B C or D): ").strip().upper()

    if response == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! Correct was {q['answer']}.\n")

print("=" * 40)
print(f"Your Final Score is {score}/{len(questions)}")
