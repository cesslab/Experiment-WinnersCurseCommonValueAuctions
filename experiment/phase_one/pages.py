import random

from phase_one._builtin import Page
from .models import Constants


class SelectAuctionPage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        auction_collection = self.player.participant.vars['phase_one_auctions']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        left_type = left_auction.atype
        right_type = right_auction.atype
        return {'left_auction': left_auction, 'right_auction': right_auction,
                'ltype': left_type, 'rtype': right_type}

    def preference_error_message(self, value):
        auction_collection = self.player.participant.vars['phase_one_auctions']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        if value not in [left_auction.aid, right_auction.aid, 0]:
            return 'You must choose Auction A, Auction B, or Indifferent'

    def before_next_page(self):
        payoff_round_a = self.player.participant.vars['round_a']
        payoff_round_b = self.player.participant.vars['round_b']
        if self.round_number == payoff_round_a or self.round_number == payoff_round_b:
            round_label = 'round_a_auction' if self.round_number == payoff_round_a else 'round_b_auction'
            auction_collection = self.player.participant.vars['phase_one_auctions']

            if self.player.preference == Constants.INDIFFERENT:
                if random.random() < 0.5:
                    self.player.participant.vars[round_label] = auction_collection.left_auction(self.round_number)
                else:
                    self.player.participant.vars[round_label] = auction_collection.right_auction(
                        self.round_number)
            else:
                self.player.participant.vars[round_label] = auction_collection.auctions[self.player.preference]


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
]
