from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from .experiment_models import Treatment


author = 'Anwar A Ruff'

doc = """
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    name_in_url = 'wc'
    players_per_group = 2
    num_rounds = 2
    auctions = Treatment.t1_auction_collection()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    preference = models.IntegerField(choices=[1, 2, 3])
