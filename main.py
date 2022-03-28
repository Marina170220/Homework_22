from question import Question
from game import Game

questions_data = Game.json_convert('questions.json')
game = Game()
table = game.data_forming(questions_data)  # Исходные данные для вывода пользователю
questions = Question.create_questions_list(questions_data)  # Список вопросов
game.rounds = len(questions)  # Количество раундов

while game.rounds > 0:
    game.print_table(table)
    user_category = game.question_return()
    is_question_exist = False

    if len(user_category) == 2:
        for question in questions:
            if user_category[0].lower() == question.category.lower() and int(
                    user_category[1]) == question.cost and not question.is_asked:
                user_answer = input(question)
                if user_answer.lower() == question.answer.lower():
                    game.points += question.cost
                    print(f'Верно, +{question.cost}. Ваш счет = {game.points}\n')
                    question.is_asked = True
                    game.correct_answers += 1
                    game.rounds -= 1
                    is_question_exist = True

                else:
                    game.points -= question.cost
                    print(f'Неверно, на самом деле – {question.answer} – {question.cost}. Ваш счет = {game.points}\n')
                    question.is_asked = True
                    game.incorrect_answers += 1
                    game.rounds -= 1
                    is_question_exist = True

        for kat, quest in table.items():  # Убираем загаданные категории из списка для вывода пользователю
            if kat.lower() == user_category[0].lower():
                for i in range(len(quest)):
                    if quest[i] == user_category[1]:
                        quest[i] = "   "
                        continue

        if not is_question_exist:
            print('Такого вопроса нет, попробуйте еще раз!\n')
    else:
        print('Категория введена некорректно. Попробуйте ещё раз!\n')

game.write_results_to_file("results.json")
game.print_results()
