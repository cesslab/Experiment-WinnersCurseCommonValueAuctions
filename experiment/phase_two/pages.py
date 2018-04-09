from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class CutoffSelectionPage(Page):
    form_model = 'player'
    form_fields = ['cutoff', 'clicked']

    def vars_for_template(self):
        auction = Constants.auctions.auction(self.round_number)
        min_max = Constants.auctions.auction_min_max(self.round_number)
        return {
            'auction': auction,
            'auction_min': min_max[0],
            'auction_max': min_max[1]}

    def cutoff_max(self):
        min_max = Constants.auctions.auction_min_max(self.round_number)
        return min_max[1]

    def cutoff_min(self):
        min_max = Constants.auctions.auction_min_max(self.round_number)
        return min_max[0]

    def error_message(self, values):
        if not int(values['clicked']) == 1:
            return 'You must make a bid for this auction.'


page_sequence = [
    InstructionsPage, CutoffSelectionPage
]
