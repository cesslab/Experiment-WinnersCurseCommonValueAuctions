from otree.api import Bot, SubmissionMustFail
from phase_one import pages

from auction.auctions import Auction


class PlayerBot(Bot):

    def play_round(self):
        participant_vars = self.player.participant.vars
        if self.round_number == 1:
            yield (pages.InstructionsPage)

        if self.round_number == 1:
            # SelectAuctionPage: test validation fails when preference is out of range
            yield SubmissionMustFail(pages.SelectAuctionPage, {'preference': 1000000})
            # SelectAuctionPage: test validation fails when preference is not selected
            yield SubmissionMustFail(pages.SelectAuctionPage)
            # SelectAuctionPage: test indifferent selection
            yield (pages.SelectAuctionPage, {'preference': 0})
            assert self.player.preference == 0
        elif self.round_number == 2:
            # SelectAuctionPage: test right preferred selection
            auction_collection = participant_vars['phase_one_auction_collection']
            right_auction = auction_collection.right_auction(self.round_number)
            yield (pages.SelectAuctionPage, {'preference': right_auction.aid})
            assert self.player.preference == right_auction.aid, "actual preference was {}".format(
                self.player.preference)
        else:
            # SelectAuctionPage: test left preferred selection
            auction_collection = participant_vars['phase_one_auction_collection']
            left_auction = auction_collection.left_auction(self.round_number)
            yield (pages.SelectAuctionPage, {'preference': left_auction.aid})
            assert self.player.preference == left_auction.aid, "actual preference was {}".format(self.player.preference)

        payoff_round_a = participant_vars['round_a']
        if self.round_number == payoff_round_a:
            assert 'auction_a_id' in participant_vars

        payoff_round_b = participant_vars['round_b']
        if self.round_number == payoff_round_b:
            assert 'auction_b_id' in participant_vars
