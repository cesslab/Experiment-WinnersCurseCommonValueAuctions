import random

from otree.api import Bot, SubmissionMustFail

from phase_two import pages


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.InstructionsPage)

        participant_vars = self.player.participant.vars
        auction_collection = participant_vars['phase_two_auction_collection']
        auction = auction_collection.auction(self.round_number)
        if self.round_number == 1:
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': - 1, 'clicked': 1})
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': auction.max_value + 1, 'clicked': 1})
            yield SubmissionMustFail(pages.CutoffSelectionPage, {'cutoff': 0, 'clicked': 0})

            yield (pages.CutoffSelectionPage, {'cutoff': 0, 'clicked': 1})
            assert self.player.cutoff == 0
        else:
            random_cutoff = random.randint(0, auction.max_value)
            yield (pages.CutoffSelectionPage, {'cutoff': random_cutoff, 'clicked': 1})
            assert self.player.cutoff == random_cutoff, "actual cutoff was {}".format(self.player.cutoff)

        assert self.player.participant.vars['auctions'][auction.aid].cutoff is not None
