import requests
import Question as Qw
import random

def get_statistics(questions):
    """Возвращает статистику по массиву вопросов."""
    statistics = {'points': 0, 'answered_questions': 0}
    for question in questions:
        if question.correct_answer == question.answer:
            statistics['points'] += question.points
            statistics['answered_questions'] += 1
    return statistics


def get_qwestion():
    """Получаем данные по вопросам и создаем объекты вопрос."""
    questions = []
    response = requests.get('https://jsonkeeper.com/b/YDW7')
    question_data = response.json()
    for question_data in question_data:
        question = Qw.Question()
        question.qw_text = question_data['q']
        question.qw_complexity = question_data['d']
        question.correct_answer = question_data['a']
        questions.append(question)
    return questions


if __name__ == '__main__':
    print('Игра начинается!')
    questions = get_qwestion()
    for question in random.sample(questions, len(questions)):
        print()
        print(f'Вопрос: {question.qw_text}')
        print(f'Сложность: {question.build_question()}')
        question.answer = input()
        print(question.build_feedback())

    response_statistics = get_statistics(questions)
    print('Вот и всё!')
    print(f'Отвечено {response_statistics["answered_questions"]} вопроса из {len(questions)}')
    print(f'Набрано баллов: {response_statistics["points"]}')
