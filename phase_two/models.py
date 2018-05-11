from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

from exp.auction.factory import AuctionFactory as Factory

author = 'Your name here'

doc = """
Phase 2:
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    # oTree Constants
    # --------------------------------------------
    name_in_url = 'phase_two'
    players_per_group = None
    num_rounds = Factory.phase_two_rounds()
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cutoff = models.DecimalField(blank=False, max_digits=4, decimal_places=2)
    auction = models.IntegerField(blank=False)
    clicked = models.IntegerField()
