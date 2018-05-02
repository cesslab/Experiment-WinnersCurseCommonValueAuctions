from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

from auction.factory import AuctionCollectionFactory as Factory

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
    num_rounds = Factory.phase_three_rounds()
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                auctions = Factory.phase_three_auction_collection()
                player.participant.vars['phase_three_auction_collection'] = auctions


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    bid = models.FloatField(blank=False)
    auction = models.IntegerField(blank=False)
    signal = models.DecimalField(blank=False, max_digits=6, decimal_places=4)
    low_update = models.DecimalField(blank=False, max_digits=6, decimal_places=4)
    high_update = models.DecimalField(blank=False, max_digits=6, decimal_places=4)
