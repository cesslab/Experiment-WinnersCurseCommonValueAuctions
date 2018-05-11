import random

from exp.auction.factory import AuctionFactory

from ._builtin import Page, WaitPage

from exp.util import Participant
from exp.auction.payment_method import PaymentMethod


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        players = self.group.get_players()[:]
        for i in range(len(players)):
            for player in players:
                other_player = random.choice(players[:i] + players[i + 1:])
                experiment = Participant.get_experiment(player)
                other_experiment = Participant.get_experiment(other_player)
                payment_method = PaymentMethod(experiment, other_experiment)

                method_one_results = payment_method.method_one_payment()
                method_two_results = payment_method.method_two_payment()


class Results(Page):
    def vars_for_template(self):
        auctions = AuctionFactory.auctions()
        aid = self.player.participant.vars['auction_a_id']

        return {'auction_1': auctions[aid]}


page_sequence = [
    ResultsWaitPage,
    Results,
]
