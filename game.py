import json


class Game:
    def __init__(self):
        self._points = 0
        self._correct_answers = 0
        self._incorrect_answers = 0
        self._question_amount = 0
        self._rounds = 0
        self._results = {}

    @property
    def points(self):
        return self._points

    @property
    def correct_answers(self):
        return self._correct_answers

    @property
    def incorrect_answers(self):
        return self._incorrect_answers

    @property
    def question_amount(self):
        return self._question_amount

    @property
    def rounds(self):
        return self._rounds

    @property
    def results(self):
        return self._results

    @points.setter
    def points(self, points: int):
        self._points = points

    @correct_answers.setter
    def correct_answers(self, num):
        self._correct_answers = num

    @incorrect_answers.setter
    def incorrect_answers(self, num):
        self._incorrect_answers = num

    @question_amount.setter
    def question_amount(self, question_amount):
        self._question_amount = question_amount

    @rounds.setter
    def rounds(self, num):
        self._rounds = num

    @staticmethod
    def json_convert(file):
        """
        Чтение данных из файла с форматом json.
        Param file: файл с данными в json-формате.
        Return: словарь с данными из файла.
        """

        with open(file, 'r') as f:
            questions_data = json.load(f)
            return questions_data

    def data_forming(self, questions_data):
        """
        Формирует исходную таблицу для вывода пользователю.
        Param questions_data: словарь с данными вопросов.
        Return: таблица с категориями и стоимостью вопросов.
        """
        table = {}
        for key, value in questions_data.items():
            count = [digit for digit in value.keys()]
            table[key] = count
        return table

    def print_table(self, table):
        """
        Выполняет отрисовку игрового поля для пользователя.
        Param table: таблица с категориями и стоимостью вопросов.
        """

        longest_category_name = 0  # Переменная-счетчик для определения максимального названия
        # категории вопроса для вывода

        for category in table.keys():
            longest_category_name = max(int(longest_category_name), len(category))

        for line in table:
            print(f'{line.ljust(longest_category_name + 1)} {"   ".join(table[line])}')

    def question_return(self):
        """
        Возвращает введенные пользователем данные в виде списка.
        Return: список выбранными категорией и стоимостью вопроса.
        """

        return (input("Выберите категорию и стоимость вопроса:\n")).split(" ")

    def write_results_to_file(self, file):
        """
        Выводит результат игры пользователя в виде словаря и записывает его в файл results.json.
        Param file: файл для записи результатов игры.
        """

        results = {"points": self.points,
                   "correct": self.correct_answers,
                   "incorrect": self.incorrect_answers
                   }

        with open(file, 'a') as f:
            json.dump(results, f)
            f.close()

    def print_results(self):
        """
        Выводит в консоль результаты игры.
        """
        print(f"""У нас закончились вопросы!
        Ваш счет - {self.points}
        Верных ответов: {self.correct_answers}
        Неправильных ответов: {self.incorrect_answers}""")
