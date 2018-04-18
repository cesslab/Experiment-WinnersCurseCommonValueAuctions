from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

author = 'Your name here'

doc = """
Phase 4: Payoff determination
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    name_in_url = 'payoffs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                auctions = Factory.phase_two_auctions()
                player.participant.vars['phase_two_auctions'] = auctions


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
