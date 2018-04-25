from ._builtin import Page
from .models import Constants


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class BidPage(Page):
    form_model = 'player'
    form_fields = ['bid']

    def vars_for_template(self):
        auction_collection = self.player.participant.vars['phase_three_auction_collection']
        auction = auction_collection.auction(self.round_number)
        signal = auction_collection.signal(self.round_number)

        return {
            'auction': auction,
            'signal': signal,
            'low_update': auction.low_update(signal),
            'high_update': auction.high_update(signal)}

    def bid_error_message(self, bid):
        auction_collection = self.player.participant.vars['phase_three_auction_collection']
        auction = auction_collection.auction(self.round_number)
        max_bid = auction.max_value
        if not 0 <= bid <= max_bid:
            return 'The bid value must be between 0 and {}.'.format(max_bid)

    def before_next_page(self):
        """
        If the auction displayed for this round is payoff relevant, the bid is saved to the participants var
        list.
        :return: None
        """
        participant_vars = self.player.participant.vars
        auction_collection = participant_vars['phase_three_auction_collection']
        auction = auction_collection.auction(self.round_number)
        signal = auction_collection.signal(self.round_number)

        assert self.player.bid is not None
        self.player.participant.vars['auctions'][auction.aid].bids[signal] = self.player.bid


page_sequence = [
    InstructionsPage, BidPage,
]
