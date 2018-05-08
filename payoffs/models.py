from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
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
    # -------------------------
    # Game Constants
    # -------------------------
    Endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 1 - Stage 1 & 3
    round_1 = models.IntegerField()
    choice_1 = models.IntegerField()
    auction_1 = models.IntegerField()
    signal_1 = models.DecimalField(max_digits=6, decimal_places=2)
    other_signal_1 = models.DecimalField(max_digits=6, decimal_places=2)
    bid_1 = models.DecimalField(max_digits=6, decimal_places=2)
    other_bid_1 = models.DecimalField(max_digits=6, decimal_places=2)
    winner_1 = models.BooleanField()
    random_low_prob_1 = models.DecimalField(max_digits=6, decimal_places=2)
    earnings_1 = models.DecimalField(max_digits=6, decimal_places=2)
    # 2 - Stage 2 & 3
    cutoff_2 = models.DecimalField(max_digits=6, decimal_places=2)
    random_cutoff_2 = models.DecimalField(max_digits=6, decimal_places=2)
    round_2 = models.IntegerField()
    auction_2 = models.IntegerField()
    choice_2 = models.IntegerField()
    signal_2 = models.DecimalField(max_digits=6, decimal_places=2)
    other_signal_2 = models.DecimalField(max_digits=6, decimal_places=2)
    bid_2 = models.DecimalField(max_digits=6, decimal_places=2)
    other_bid_2 = models.DecimalField(max_digits=6, decimal_places=2)
    winner_2 = models.BooleanField()
    random_low_prob_2 = models.DecimalField(max_digits=6, decimal_places=2)
    earnings_2 = models.DecimalField(max_digits=6, decimal_places=2)
