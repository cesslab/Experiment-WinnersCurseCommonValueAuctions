from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from auction.auctions import AuctionCollectionFactory


author = 'Anwar A Ruff'

doc = """
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    # oTree Constants
    # --------------------------------------------
    name_in_url = 'wc'
    players_per_group = 2
    num_rounds = 2
    # Experiment Constants
    # --------------------------------------------
    auctions = AuctionCollectionFactory.phase_one_auctions()
    A = 1
    NEITHER = 2
    B = 3
    INSTRUCTIONS_ROUND = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    preference = models.IntegerField(choices=[1, 2, 3])