import json


def json_convert(file):
    """Функция производит чтение данных из файла с форматом .json """

    with open(file, 'r') as f:
        questions = json.load(f)
    return questions


def data_forming(questions):
    ''' Функция формирует исходную таблицу для вывода пользователю'''

    table = {}
    for key, value in questions.items():
        count = []
        for digit in value.keys():
            count.append(digit)
        table[key] = count
    return table


def question_return():
    """Функция возвращает введенные пользователем данные в формате, приемлемом для работы программы без ошибок"""

    user_data = input("Выберите категорию и стоимость вопроса:\n")
    choosed_question = user_data.split(" ")
    choosed_question[0] = choosed_question[0].title()
    return choosed_question


def results(points, correct, incorrect):
    """Функция выводит результат игры пользователя и записывает результаты в файл results.json"""

    result = json.dumps({'points': points, 'correct': correct, 'incorrect': incorrect})

    with open('results.json', 'a') as file:
        file.write(result)
        file.write('\n')

    print(f"""У нас закончились вопросы!
  
Ваш счет - {points}
Верных ответов: {correct}
Неправильных ответов: {incorrect}""")


def print_table(table):
    """Выполняет отрисовку игрового поля для пользователя"""

    lenght = 0  # Переменная-счетчик для определения длины строки категории вопроса для вывода

    for key in table.keys():
        lenght = max(int(lenght), len(key))

    for line in table:
        print(f'{line.ljust(lenght + 1)} {"   ".join(table[line])}')


def answers_quality(quantity, questions):
    """Функция производит подсчет правильных и неправильных ответов"""

    correct = 0
    for i in questions.values():
        for n in i.values():
            if n['asked'] == True:
                correct += 1
    incorrect = quantity - correct

    return correct, incorrect


def questions_quantity(table):
    """Функция возвращает колиечство воспросв в игре"""

    quantity = 0
    for value in on_board.values():
        quantity += len(value)

    return quantity


questions = json_convert('questions.json')  # Список вопросов

on_board = data_forming(questions)  # Исходные данные для вывода пользователю

quantity = questions_quantity(on_board)  # Количество вопросов

scores = 0  # Переменная-счетчик очков в игре

for i in range(quantity):
    print_table(on_board)  # Вывод таблицы пользователю

    choosed_question = question_return()  # Выбор пользователем вопроса и стоимости

    if choosed_question[0] in questions.keys():
        if choosed_question[1] in on_board[choosed_question[0]]:

            print(f'Слово {questions[choosed_question[0]][choosed_question[1]]["question"]} в переводе означает?')
            answer = input()
            answer = answer.lower()

            if answer == questions[choosed_question[0]][choosed_question[1]]['answer']:  # Ответ верный
                scores += int(choosed_question[1])
                questions[choosed_question[0]][choosed_question[1]]["asked"] = True
                print(f'Верно! +{choosed_question[1]}. Ваш счет = {scores}\n')

            else:  # Ответ неверный
                scores -= int(choosed_question[1])
                print(
                    f"Неверно, на самом деле - {questions[choosed_question[0]][choosed_question[1]]['answer']}. - {choosed_question[1]}. Ваш счет = {scores}\n")
                questions[choosed_question[0]][choosed_question[1]]["asked"] = False
            on_board[choosed_question[0]][on_board[choosed_question[0]].index(choosed_question[1])] = '   '

        else:  # Пользователь указал несуществующую стоимость вопроса
            print("Вопроса с такой стоимостью нет, попробуйте еще раз\n")

    else:  # Пользователь указал несуществующую категорию
        print("Такой категории нет, попробуйте еще\n")

results(scores, answers_quality(quantity, questions)[0],
        answers_quality(quantity, questions)[1])  # Вывод результата иигры пользователю
