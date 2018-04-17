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
        auction_collection = self.player.participant.vars['phase_three_auctions']
        auction = auction_collection.auction(self.round_number)
        signal = auction_collection.signal(self.round_number)

        return {
            'auction': auction,
            'signal': signal,
            'low_update': auction.low_update(signal),
            'high_update': auction.high_update(signal)}

    def bid_min(self):
        return 0

    def bid_max(self):
        auction_collection = self.player.participant.vars['phase_three_auctions']
        auction = auction_collection.auction(self.round_number)
        return auction.max_value


class Results(Page):
    pass


page_sequence = [
    InstructionsPage, BidPage,
]
