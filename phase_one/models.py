import random

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
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
    players_per_group = None
    num_rounds = Factory.phase_one_rounds()
    # --------------------------------------------
    # Experiment Constants
    # --------------------------------------------
    INSTRUCTIONS_ROUND = 1
    INDIFFERENT = 0


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                phase_one_auction_collection = Factory.phase_one_auction_collection()
                player.participant.vars['phase_one_auction_collection'] = phase_one_auction_collection
                player.participant.vars['auctions'] = Factory.auctions()

                rounds = list(range(1, Constants.num_rounds + 1))
                random.shuffle(rounds)
                player.participant.vars['round_a'] = rounds.pop()
                player.participant.vars['round_b'] = rounds.pop()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    preference = models.IntegerField(blank=False)
    left_auction = models.IntegerField(blank=False)
    right_auction = models.IntegerField(blank=False)
