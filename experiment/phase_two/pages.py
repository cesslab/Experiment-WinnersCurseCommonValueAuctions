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
        auction_collection = self.player.participant.vars['phase_one_auctions']
        auction = auction_collection.auction(self.round_number)
        return {
            'auction': auction,
            'auction_min': auction.min,
            'auction_max': auction.max}

    def cutoff_max(self):
        auction_collection = self.player.participant.vars['phase_one_auctions']
        auction = auction_collection.auction(self.round_number)
        return auction.max

    def cutoff_min(self):
        auction_collection = self.player.participant.vars['phase_one_auctions']
        auction = auction_collection.auction(self.round_number)
        return auction.min

    def error_message(self, values):
        if not int(values['clicked']) == 1:
            return 'You must make a bid for this auction.'


page_sequence = [
    InstructionsPage, CutoffSelectionPage
]
