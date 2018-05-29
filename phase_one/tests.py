import random

from otree.api import Bot, SubmissionMustFail
from phase_one import pages, models
from exp.util import Participant


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

            yield SubmissionMustFail(pages.SelectAuctionPage, {'preference': 1000000})
            yield SubmissionMustFail(pages.SelectAuctionPage)
            yield (pages.SelectAuctionPage, {'preference': -1})
            assert self.player.preference == -1
        else:
            phase_one = Participant.get_experiment(self.player).phase_one
            auction_ids = [
                phase_one.left_auction(self.round_number).aid,
                phase_one.right_auction(self.round_number).aid,
                -1]
            print(auction_ids)
            random_auction_id = random.choice(auction_ids)

            yield (pages.SelectAuctionPage, {'preference': random_auction_id})

            assert self.player.preference == random_auction_id, "actual preference was {}".format(self.player.preference)

            auction_id = phase_one.get_preference(self.round_number)
            assert random_auction_id == auction_id, "expected {}, but received {}".format(random_auction_id, auction_id)

