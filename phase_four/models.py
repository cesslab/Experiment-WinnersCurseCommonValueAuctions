from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'phase_four'
    players_per_group = None
    num_rounds = 6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    die_side = models.IntegerField(blank=False)
    bet = models.IntegerField(blank=False)
    cutoff = models.DecimalField(blank=False, max_digits=4, decimal_places=2)
    clicked = models.IntegerField()
    lottery = models.IntegerField(blank=False)
