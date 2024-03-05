import json

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["question"])

        for i, option in enumerate(question["options"], start = 1):
            print(f"{i}. {option}")

        user_answer = input("Your answer [option number]: ")

        if(int(user_answer) not in range(1, 5)):
            print("invalid input")
            return

        return int(user_answer)

    def start_quiz(self):
        for question in self.questions:
            user_answer = self.display_question(question)
            correct_answer = question["correct_option"]

            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}: {question['options'][correct_answer - 1]}\n")

        print(f"Quiz completed! Your score is: {self.score}/{len(self.questions)}")


def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

questions_list = load_questions("./questions.json")

quiz = Quiz(questions_list)
quiz.start_quiz()
