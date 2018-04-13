from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from auction.factory import AuctionCollectionFactory

author = 'Your name here'

doc = """
Phase 2:
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    # oTree Constants
    # --------------------------------------------
    name_in_url = 'phase_two'
    players_per_group = 2
    num_rounds = AuctionCollectionFactory.phase_two_rounds()
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1
    auctions = AuctionCollectionFactory.phase_two_auctions()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cutoff = models.IntegerField(blank=False)
    clicked = models.IntegerField()
