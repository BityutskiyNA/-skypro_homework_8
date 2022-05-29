class Question:

    def __init__(self):
       self.__qw_text = None
       self.__qw_complexity = None
       self.__correct_answer = None
       self.__question_asked = False
       self.__answer = None
       self.__points = 0

    @property
    def qw_text(self):
        return self.__qw_text

    @qw_text.setter
    def qw_text(self, qw_text):
        self.__qw_text = qw_text

    @property
    def qw_complexity(self):
        return self.__qw_complexity

    @qw_complexity.setter
    def qw_complexity(self, qw_complexity):
        self.__qw_complexity = int(qw_complexity)
        self.set_points()

    @property
    def correct_answer(self):
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer

    @property
    def points(self):
       return self.__points

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        self.__answer = answer

    def set_points(self):
       """Возвращает int, количество баллов.
       Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов."""
       self.__points = self.__qw_complexity * 10


    def is_correct(self):
       """Возвращает True, если ответ пользователя совпадает
       с верным ответов иначе False."""
       if self.__correct_answer == self.__answer:
           return True
       else:
           return False


    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
         Вопрос: What do people often call American flag? Сложность 4/5"""
        return f'{self.qw_text} Сложность {self.__qw_complexity}/5'


    def build_feedback(self):
        """Возвращает если ответ верный: Ответ верный, получено __ баллов
        и устанавливает self.question_asked = True
           Возвращает если ответ не верный: Ответ неверный, верный ответ __"""
        self.question_asked = True
        if self.is_correct():
            return f'Ответ верный, получено {self.__points} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.__correct_answer}'
