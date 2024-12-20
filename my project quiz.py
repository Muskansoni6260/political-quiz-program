#Quiz game

import random


# this is our Political questions Quiz Game

def print_welcome_message():
    print("Welcome to the Political Quiz Game!")
    print("Test your knowledge about politics and world leaders.")
    print("Let's begin!\n")


def question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    answer = input("Enter the number of your answer: ")

    if answer == str(correct_option):
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer was: {options[correct_option - 1]}\n")
        return False


def political_quiz():
    score = 0
    total_questions = 5

    questions = [
        {
            "question": "Who was the first President of the United States?",
            "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
            "correct_option": 1
        },
        {
            "question": "Which country is known for the political concept of Communism?",
            "options": ["United States", "China", "Russia", "Cuba"],
            "correct_option": 3
        },
        {
            "question": "Who was the Prime Minister of the UK during World War II?",
            "options": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Margaret Thatcher"],
            "correct_option": 1
        },
        {
            "question": "Which political party did Barack Obama belong to?",
            "options": ["Republican", "Democratic", "Independent", "Green Party"],
            "correct_option": 2
        },
        {
            "question": "Who is the current Chancellor of Germany (as of 2024)?",
            "options": ["Angela Merkel", "Olaf Scholz", "Emmanuel Macron", "Ursula von der Leyen"],
            "correct_option": 2
        }
    ]

    print_welcome_message()

    # jumbled the questions
    random.shuffle(questions)


    for i in range(total_questions):
        question_data = questions[i]
        correct = question(question_data["question"], question_data["options"], question_data["correct_option"])
        if correct:
            score += 1

    print(f"your Game is Over! Your score is {score}/{total_questions}.")

    if score == total_questions:
        print("Excellent! You're a political expert!")
    elif score >= total_questions // 2:
        print("Good job! You know your politics.")
    else:
        print("You might want to study more about politics!")


# Start the quiz game
if __name__ == "__main__":
    political_quiz()
def open_and_read_file(file_name):
    """
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found. Please check the file name or path."
    except Exception as e:
        return f"Error: {e}"

# Example usage
file_name = "my project quiz.txt"
file_content = open_and_read_file(file_name)

print(file_content)

