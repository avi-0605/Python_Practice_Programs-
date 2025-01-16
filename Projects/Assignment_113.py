#Quiz Game Build a simple quiz game that asks multiple-choice questions and tracks the score.
def quiz_game():
    score = 0
    questions = [
        ("What is the capital of France?", "Paris"),
        ("Which planet is known as the Red Planet?", "Mars"),
        ("What is the largest ocean?", "Pacific"),
        ("Who wrote 'Romeo and Juliet'?", "Shakespeare")
    ]
    
    for question, correct_answer in questions:
        answer = input(f"{question} ")
        if answer.lower() == correct_answer.lower():
            score += 1
    
    print(f"Your score is: {score}/{len(questions)}")

# Start the quiz
quiz_game()
