from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from auction.auctions import AuctionCollectionFactory

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
    num_rounds = 1
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1
    auctions = AuctionCollectionFactory.phase_two_auctions()
    MIN_BID = 0
    MAX_BID = 100
    BID_INCREMENTS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    bid = models.IntegerField(
        min=Constants.MIN_BID, max=Constants.MAX_BID,
        widget=widgets.Slider({'step': '1'}), blank=False)
