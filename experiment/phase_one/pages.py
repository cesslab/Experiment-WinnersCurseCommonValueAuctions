import random

from phase_one._builtin import Page
from .models import Constants


class SelectAuctionPage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        auction_collection = self.player.participant.vars['phase_one_auction_collection']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        left_type = left_auction.atype
        right_type = right_auction.atype
        return {'left_auction': left_auction, 'right_auction': right_auction,
                'ltype': left_type, 'rtype': right_type}

    def preference_error_message(self, value):
        auction_collection = self.player.participant.vars['phase_one_auction_collection']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        if value not in [left_auction.aid, right_auction.aid, 0]:
            return 'You must choose Auction A, Auction B, or Indifferent'

    def before_next_page(self):
        """
        If this round is payoff relevant the preferred Auction is saved to the participants var
        list. If the subjects did not have a preference then one of the two auctions show is
        selected at random.

        Note: This function is executed by each player before leaving the Select Auction Screen.

        :return: None
        """
        round_a = self.player.participant.vars['round_a']
        participant_vars = self.player.participant.vars

        if self.round_number == round_a:
            auction_collection = participant_vars['phase_one_auction_collection']
            if self.player.preference == Constants.INDIFFERENT:
                if random.random() < 0.5:
                    participant_vars['auction_a_id'] = auction_collection.left_auction(self.round_number).aid
                else:
                    participant_vars['auction_a_id'] = auction_collection.right_auction(self.round_number).aid
            else:
                participant_vars['auction_a_id'] = self.player.preference

        payoff_round_b = participant_vars['round_b']
        if self.round_number == payoff_round_b:
            auction_collection = participant_vars['phase_one_auction_collection']
            if self.player.preference == Constants.INDIFFERENT:
                if random.random() < 0.5:
                    participant_vars['auction_b_id'] = auction_collection.left_auction(self.round_number).aid
                else:
                    participant_vars['auction_b_id'] = auction_collection.right_auction(self.round_number).aid
            else:
                participant_vars['auction_b_id'] = self.player.preference


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
