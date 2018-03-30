from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from auction.auctions import AuctionCollectionFactory

author = 'Your name here'

doc = """
Your app description
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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
