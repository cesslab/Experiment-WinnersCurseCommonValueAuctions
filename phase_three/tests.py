import random

from otree.api import Bot, SubmissionMustFail
from phase_three import pages
from exp.util import Participant


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

            max_value = Participant.get_experiment(self.player).phase_three.auction(self.player.round_number).max_value
            yield SubmissionMustFail(pages.BidPage, {'bid': - 1})
            yield SubmissionMustFail(pages.BidPage, {'bid': max_value + 1})
            yield SubmissionMustFail(pages.BidPage)

            yield (pages.BidPage, {'bid': 0})
            assert self.player.bid == 0
        else:
            max_value = Participant.get_experiment(self.player).phase_three.auction(self.player.round_number).max_value
            r_bid = random.randint(0, max_value)
            yield (pages.BidPage, {'bid': r_bid})
            assert self.player.bid == r_bid, "Entered bid {}, Player bid {}".format(r_bid, self.player.bid)

            signal = Participant.get_experiment(self.player).phase_three.signal(self.player.round_number)
            bid = Participant.get_experiment(self.player).phase_three.auction(self.player.round_number).get_bid(signal)
            assert bid == r_bid, "Entered bid {}, Auction bid {}".format(r_bid, bid)

