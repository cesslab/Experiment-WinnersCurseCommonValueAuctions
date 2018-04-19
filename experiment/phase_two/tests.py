import random

from otree.api import Bot, SubmissionMustFail

from phase_two import pages


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

        if self.round_number == 1:
            auction_collection = self.player.participant.vars['phase_two_auctions']
            auction = auction_collection.auction(self.round_number)

            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': - 1, 'clicked': 1})
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': auction.max_value + 1, 'clicked': 1})
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': 0, 'clicked': 0})

            yield (pages.CutoffSelectionPage, {'cutoff': 0, 'clicked': 1})
            assert self.player.cutoff == 0
        else:
            auction_collection = self.player.participant.vars['phase_two_auctions']
            auction = auction_collection.auction(self.round_number)

            random_cutoff = random.randint(0, auction.max_value)

            yield (pages.CutoffSelectionPage, {'cutoff': random_cutoff, 'clicked': 1})
            assert self.player.cutoff == random_cutoff, "actual cutoff was {}".format(self.player.cutoff)
