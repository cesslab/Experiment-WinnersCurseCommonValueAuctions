from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class QuestionnairePage(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'major', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']


page_sequence = [
    QuestionnairePage,
]
