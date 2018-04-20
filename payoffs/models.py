from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

author = 'Anwar A. Ruff'

doc = """
Phase 4: Payoff determination
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    name_in_url = 'payoffs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
