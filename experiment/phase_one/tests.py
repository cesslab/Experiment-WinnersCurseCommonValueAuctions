from auction._builtin import Bot
from phase_one import pages


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.InstructionsPage)
        yield (pages.SelectAuctionPage, {'preference': 0})
