
def read_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 6):
            question = lines[i].strip()
            options = [lines[i + j].strip() for j in range(1, 5)]
            correct_answer = lines[i + 5].strip()
            questions.append((question, options, correct_answer))
    return questions

def play_quiz(questions):
    score = 0
    for i, (question, options, correct_answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        for j, option in enumerate(options, 1):
            print(f"{chr(64 + j)}) {option}")
        player_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if player_answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}")
        print(f"Your score: {score}\n")
    print(f"Quiz completed! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_file = r"C:\Users\nandh\Desktop\Quize_Questions.txt"
    quiz_questions = read_questions(quiz_file)
    play_quiz(quiz_questions)

