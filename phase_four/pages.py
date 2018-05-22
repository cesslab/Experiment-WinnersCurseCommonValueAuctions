from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage(Page):
    pass


class RollDicePage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


page_sequence = [
    InstructionsPage,
    RollDicePage,
    ResultsWaitPage,
]