import random

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

from exp.auction.factory import AuctionFactory as Factory
from exp.experiment import Experiment
from exp.util import Participant


author = 'Anwar A Ruff'

doc = """
Phase 1:
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    # oTree Constants
    # --------------------------------------------
    name_in_url = 'wc'
    players_per_group = None
    num_rounds = Factory.phase_one_rounds()
    # --------------------------------------------
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1
    INDIFFERENT = 0


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                Participant.set_experiment(player, Experiment())


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    preference = models.IntegerField(blank=False)
    left_auction = models.IntegerField(blank=False)
    right_auction = models.IntegerField(blank=False)
