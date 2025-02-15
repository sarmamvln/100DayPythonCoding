from langchain.chains.qa_with_sources.map_reduce_prompt import question_prompt_template


class QuestionModal:
    def __init__(self, question, answer):
        self.question= question
        self.answer= answer



