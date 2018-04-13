from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from auction.factory import AuctionCollectionFactory as Factory


author = 'Anwar A Ruff'

doc = """
Phase 1:
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    # oTree Constants
    # --------------------------------------------
    name_in_url = 'wc'
    players_per_group = 2
    num_rounds = Factory.phase_one_rounds()
    # --------------------------------------------
    # Experiment Constants
    # --------------------------------------------
    auctions = Factory.phase_one_auctions()
    A = 1
    NEITHER = 2
    B = 3
    INSTRUCTIONS_ROUND = 1
    PREFERENCE_OPTIONS = [1, 2, 3]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['phase_1_auctions'] = Factory.phase_one_auctions()



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    preference = models.IntegerField(choices=Constants.PREFERENCE_OPTIONS, blank=False)
