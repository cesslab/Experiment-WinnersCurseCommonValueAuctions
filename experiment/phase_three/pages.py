from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class BidPage(Page):
    form_model = 'player'
    form_fields = ['bid']

    def vars_for_template(self):
        auction = Constants.auctions.auction(self.round_number)
        signal = Constants.auctions.signal(self.round_number)
        return {'auction': auction, 'signal': signal}


class Results(Page):
    pass


page_sequence = [
    InstructionsPage, BidPage,
]
