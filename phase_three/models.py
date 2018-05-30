from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

from exp.experiment import Experiment

author = 'Your name here'

doc = """
Phase 3:
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    # oTree Constants
    # --------------------------------------------
    name_in_url = 'phase_three'
    players_per_group = None
    num_rounds = Experiment.phase_three_rounds()
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    bid = models.FloatField(blank=False)
    auction = models.IntegerField(blank=False)
    signal = models.FloatField(blank=False)
    low_update = models.FloatField(blank=False)
    high_update = models.FloatField(blank=False)
