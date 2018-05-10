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
        return {
            'left_auction': left_auction,
            'right_auction': right_auction,
            'ltype': left_type,
            'rtype': right_type}

    def preference_error_message(self, value):
        auction_collection = self.player.participant.vars['phase_one_auction_collection']
        left_auction = auction_collection.left_auction(self.round_number)
        right_auction = auction_collection.right_auction(self.round_number)
        if value not in [left_auction.aid, right_auction.aid, 0]:
            return 'You must choose Auction A, Auction B, or Indifferent'

    def before_next_page(self):
        """
        Save data to player model, and to participant vars for payoff calculation
        """
        round_a = self.player.participant.vars['round_a']
        participant_vars = self.player.participant.vars

        self.set_left_right_auctions()

        if self.round_number == round_a:
            self.set_payment_round_auction_id(participant_vars, 'auction_a_id')

        round_b = participant_vars['round_b']
        if self.round_number == round_b:
            self.set_payment_round_auction_id(participant_vars, 'auction_b_id')

    def set_left_right_auctions(self):
        auction_collection = self.player.participant.vars['phase_one_auction_collection']
        self.player.left_auction = auction_collection.left_auction(self.round_number).aid
        self.player.right_auction = auction_collection.right_auction(self.round_number).aid

    def set_payment_round_auction_id(self, participant_vars, auction_id):
        self.player.participant.vars[auction_id + '_choice'] = self.player.preference
        auction_collection = participant_vars['phase_one_auction_collection']
        if self.player.preference == Constants.INDIFFERENT:
            if random.random() < 0.5:
                participant_vars[auction_id] = auction_collection.left_auction(self.round_number).aid
            else:
                participant_vars[auction_id] = auction_collection.right_auction(self.round_number).aid
        else:
            participant_vars[auction_id] = self.player.preference

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
