from ._builtin import Page
from .models import Constants


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class CutoffSelectionPage(Page):
    form_model = 'player'
    form_fields = ['cutoff', 'clicked']

    def vars_for_template(self):
        auction_collection = self.player.participant.vars['phase_two_auction_collection']
        auction = auction_collection.auction(self.round_number)
        return {'auction': auction}

    def cutoff_max(self):
        auction_collection = self.player.participant.vars['phase_two_auction_collection']
        auction = auction_collection.auction(self.round_number)
        return auction.max_value

    def cutoff_min(self):
        return 0

    def error_message(self, values):
        if not int(values['clicked']) == 1:
            return 'You must make a bid for this auction.'

    def before_next_page(self):
        """
        If the auction displayed for this round is payoff relevant, the cutoff is saved to the participants var
        list.
        :return: None
        """
        participant_vars = self.player.participant.vars
        auction_collection = self.player.participant.vars['phase_two_auction_collection']
        auction = auction_collection.auction(self.round_number)
        participant_vars['auctions'][auction.aid].cutoff = self.player.cutoff


page_sequence = [
    InstructionsPage, CutoffSelectionPage
]
