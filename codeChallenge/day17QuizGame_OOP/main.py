from question_model import  QuestionModal
from data import  question_data
from quiz_brain import QuestionBank


question_modal = []
for each in question_data:
    question= each["text"]
    answer= each["answer"]
    new_question= QuestionModal(question, answer)
    question_modal.append(new_question)

quiz= QuestionBank(question_modal)

while quiz.stllhasquestions():
    quiz.nextquestion()

#print(question_modal )

print("you completed quiz")
print(f"your final score; {quiz.score}/{quiz.questionNumber}")