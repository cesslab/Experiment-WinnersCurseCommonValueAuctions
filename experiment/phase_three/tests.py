import random

from otree.api import Bot, SubmissionMustFail

from phase_three import pages


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

        if self.round_number == 1:
            auction_collection = self.player.participant.vars['phase_three_auctions']
            auction = auction_collection.auction(self.round_number)

            yield SubmissionMustFail(pages.BidPage, {'bid': - 1})
            yield SubmissionMustFail(pages.BidPage, {'bid': auction.max_value + 1})
            yield SubmissionMustFail(pages.BidPage)

            yield (pages.BidPage, {'bid': 0})
            assert self.player.bid == 0
        else:
            auction_collection = self.player.participant.vars['phase_three_auctions']
            auction = auction_collection.auction(self.round_number)

            random_bid = random.randint(0, auction.max_value)

            yield (pages.BidPage, {'bid': random_bid})
            assert self.player.bid == random_bid, "actual bid was {}".format(self.player.bid)
