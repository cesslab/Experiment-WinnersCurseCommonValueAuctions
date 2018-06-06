from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class QuizPage(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']

    def q1_error_message(self, value):
        if value != 3:
            return 'Incorrect answer for question 1. Please try again.'

    def q2_error_message(self, value):
        if value != 2:
            return 'Incorrect answer for question 2. Please try again.'

    def q3_error_message(self, value):
        if value != 3:
            return 'Incorrect answer for question 3. Please try again.'

    def q4_error_message(self, value):
        if value != 3:
            return 'Incorrect answer for question 4. Please try again.'

    def q5_error_message(self, value):
        if value != 3:
            return 'Incorrect answer for question 5. Please try again.'

    def error_messages(self, values):
        print(values['q6'])
        if not (1 in values['q6'] and 2 in values['q6'] and 3 in values['p6']):
            return 'Incorrect answer for question 6. Please try again.'


page_sequence = [
    QuizPage,
]
