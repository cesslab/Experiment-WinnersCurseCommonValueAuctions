import random

from otree.api import Bot, SubmissionMustFail
from phase_two import pages
from core.util import Participant


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

            max_value = Participant.get_experiment(self.player).phase_two.get_auction(self.player.round_number).max_value
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': - 1, 'clicked': 1})
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': max_value + 1, 'clicked': 1})

            yield (pages.CutoffSelectionPage, {'cutoff': 0, 'clicked': 1})
            assert self.player.cutoff == 0
        else:
            max_value = Participant.get_experiment(self.player).phase_two.get_auction(self.player.round_number).max_value
            r_cutoff = random.randint(0, max_value)
            yield (pages.CutoffSelectionPage, {'cutoff': r_cutoff, 'clicked': 1})
            assert self.player.cutoff == r_cutoff, "Entered cutoff {}, Player cutoff {}".format(r_cutoff, self.player.cutoff)

            cutoff = Participant.get_experiment(self.player).phase_two.get_auction(self.player.round_number).cutoff
            assert cutoff == r_cutoff, "Entered cutoff {}, Auction cutoff {}".format(r_cutoff, cutoff)


