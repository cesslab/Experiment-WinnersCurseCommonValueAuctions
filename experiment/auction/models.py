from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Anwar A Ruff'

doc = """
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Auction:
    def __init__(self, val_low, val_high, prob_low, prob_high):
        self.val_low = val_low
        self.val_high = val_high
        self.prob_low = prob_low
        self.prob_high = prob_high


class Constants(BaseConstants):
    name_in_url = 'wc'
    players_per_group = 2
    num_rounds = 1
    auctions = [
        [
            Auction(val_low=[0.2], val_high=[0.2], prob_low=[0.4], prob_high=[0.7]),
            Auction(val_low=[0.1], val_high=[0.3], prob_low=[0.7], prob_high=[0.1])
        ],
        [
            Auction(val_low=[0.2], val_high=[0.2], prob_low=[0.4], prob_high=[0.7]),
            Auction(val_low=[0.1], val_high=[0.3], prob_low=[0.7], prob_high=[0.1])
        ],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
