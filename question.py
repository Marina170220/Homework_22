class Question:
    def __init__(self, category, question_text, answer, cost):
        self._category = category
        self._question_text = question_text
        self._answer = answer
        self._cost = cost
        self._is_asked = False

    @staticmethod
    def create_questions_list(questions_data):
        """
        Создаёт список объектов класса Question.
        Param questions_data: словарь с данными вопросов.
        Return: список вопросов.
        """
        questions = []
        for key, value in questions_data.items():
            for cost, question in value.items():
                questions.append(Question(key, question["question"], question["answer"], int(cost)))

        return questions

    @property
    def category(self):
        return self._category

    @property
    def question_text(self):
        return self._question_text

    @property
    def answer(self):
        return self._answer

    @property
    def cost(self):
        return self._cost

    @property
    def is_asked(self):
        return self._is_asked

    @is_asked.setter
    def is_asked(self, is_asked):
        self._is_asked = is_asked

    def __str__(self):
        return f"""Слово {self._question_text} в переводе означает?\n"""
