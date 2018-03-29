from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from phase_one.experiment_models import Treatment

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'phase_two'
    players_per_group = 2
    num_rounds = 1
    # --------------------------------------------
    # constants
    # --------------------------------------------
    auctions = Treatment.t1_auction_collection()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
