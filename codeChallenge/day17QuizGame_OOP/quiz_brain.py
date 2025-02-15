
class QuestionBank:
    def __init__(self, q_list):
        self.score=0
        self.questionNumber= 0;
        self.qestionlist= q_list

    def stllhasquestions(self):
        return self.questionNumber < len(self.qestionlist)

    def nextquestion(self):
        currenyquestion = self.qestionlist[self.questionNumber]
        self.questionNumber+=1
        useranswer= input(f"Q.{self.questionNumber}: {currenyquestion.question}  (True/False): ");
        self.checkanser(useranswer, currenyquestion.answer)

    def checkanser(self, user_namser, correct_answer):
        if user_namser.lower()==correct_answer.lower():
            self.score+=1
            print("you got it")

        else:
            print("this is worng")
        print(f"The correct answer was: {correct_answer}")
        print(f"your current score is: {self.score}/{self.questionNumber}")
        print()