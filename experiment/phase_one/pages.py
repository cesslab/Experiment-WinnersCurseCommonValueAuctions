from otree.api import Currency as c, currency_range
from phase_one._builtin import Page, WaitPage
from .models import Constants


class SelectAuctionPage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        auction_collection = self.player.participant.vars['phase_one_auctions']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        return {'left_auction': left_auction, 'right_auction': right_auction}

    def preference_error_message(self, value):
        auction_collection = self.player.participant.vars['phase_one_auctions']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        if value not in [left_auction.id, right_auction.id, 0]:
            return 'You must choose Auction A, Auction B, or Indifferent'


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class Results(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False


page_sequence = [
    InstructionsPage,
    SelectAuctionPage,
    # ResultsWaitPage,
    # Results
]
