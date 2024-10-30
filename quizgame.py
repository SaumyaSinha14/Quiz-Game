# Basic Quiz Game

def ask_question(question, options, correct_answer):
    """
    Function to ask a question and return if the answer is correct.
    
    Parameters:
    question (str): The question to be asked.
    options (list): List of answer options.
    correct_answer (str): The correct answer.
    
    Returns:
    bool: True if the answer is correct, False otherwise.
    """
    print(question)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
        
    answer = input("Please enter the number of your answer: ")
    
    # Check if the input is valid
    try:
        answer_index = int(answer) - 1
        if answer_index < 0 or answer_index >= len(options):
            print("Invalid option. Please choose a valid option.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False
    
    if options[answer_index] == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")
        return False


def main():
    """
    Main function to run the quiz game.
    """
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    print("---------------------------")

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"\nYour total score is: {score} out of {len(questions)}")
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
