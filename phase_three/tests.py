import random

from otree.api import Bot, SubmissionMustFail

from phase_three import pages


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

        auction_collection = self.player.participant.vars['phase_three_auction_collection']
        auction = auction_collection.auction(self.round_number)
        if self.round_number == 1:
            yield SubmissionMustFail(pages.BidPage, {'bid': - 1})
            yield SubmissionMustFail(pages.BidPage, {'bid': auction.max_value + 1})
            yield SubmissionMustFail(pages.BidPage)

            yield (pages.BidPage, {'bid': 0})
            assert self.player.bid == 0
        else:
            random_bid = random.randint(0, auction.max_value)
            yield (pages.BidPage, {'bid': random_bid})
            assert self.player.bid == random_bid, "actual bid was {}".format(self.player.bid)

        auction_a = self.player.participant.vars['auction_a']
        if auction.aid == auction_a.aid:
            assert 'bid_a' in self.player.participant.vars

        auction_b = self.player.participant.vars['auction_b']
        if auction.aid == auction_b.aid:
            assert 'bid_b' in self.player.participant.vars
