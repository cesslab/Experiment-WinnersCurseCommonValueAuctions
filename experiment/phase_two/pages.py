from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage(Page):
    pass


class CutoffSelectionPage(Page):
    form_model = 'player'
    form_fields = ['bid']

    def vars_for_template(self):
        auction = Constants.auctions.auction(self.round_number)
        return {'auction': auction}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    InstructionsPage, CutoffSelectionPage
]
