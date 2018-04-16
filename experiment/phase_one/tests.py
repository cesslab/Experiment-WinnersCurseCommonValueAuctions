from otree.api import Bot, SubmissionMustFail
from phase_one import pages


class PlayerBot(Bot):

    def play_round(self):
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
            auction_collection = self.player.participant.vars['phase_one_auctions']
            right_auction = auction_collection.right_auction(self.round_number)
            yield (pages.SelectAuctionPage, {'preference': right_auction.id})
            assert self.player.preference == right_auction.id, "actual preference was {}".format(self.player.preference)
        else:
            # SelectAuctionPage: test left preferred selection
            auction_collection = self.player.participant.vars['phase_one_auctions']
            left_auction = auction_collection.left_auction(self.round_number)
            yield (pages.SelectAuctionPage, {'preference': left_auction.id})
            assert self.player.preference == left_auction.id, "actual preference was {}".format(self.player.preference)



