from otree.api import Bot
from payoffs import pages, models


class PlayerBot(Bot):
    def play_round(self):
        yield (pages.MethodOneResults)
        assert self.player.payoff is not None
