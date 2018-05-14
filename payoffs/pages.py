import random

from ._builtin import Page, WaitPage

from exp.util import Participant
from exp.payment import PaymentMethod


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        players = self.group.get_players()[:]
        for i in range(len(players)):
            for player in players:
                player_id = player.participant.id_in_session
                other_player = random.choice(players[:i] + players[i + 1:])
                other_id = other_player.participant.id_in_session
                experiment = Participant.get_experiment(player)
                other_experiment = Participant.get_experiment(other_player)
                payment_method = PaymentMethod(player_id, other_id, experiment, other_experiment)

                Participant.set_payment_one_results(player, payment_method.method_one_payment())
                Participant.set_payment_two_results(player, payment_method.method_two_payment())


class PaymentOneResults(Page):
    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        results = Participant.get_payment_one_results(self.player)

        random_position = ''
        if results.preferred_position == experiment.phase_one.LEFT:
            preferred_position = 'Left'
        elif results.preferred_position == experiment.phase_one.RIGHT:
            preferred_position = 'Right'
        else:
            preferred_position = 'Indifferent'
            random_position = 'Left' if results.left_auction.aid == results.auction.aid else 'Right'

        return {
            'preferred_position': preferred_position,
            'left_auction': results.left_auction,
            'right_auction': results.right_auction,
            'auction': results.auction,
            'random_position': random_position,
            'bid': results.bid,
            'others_bid': results.other_bid,
            'winner': results.win_lottery,
            'signal': results.random_signal,
            'others_signal': results.other_random_signal,
            'low_value': results.low_value,
            'high_value': results.high_value,
            'low_prob': results.low_prob * 100,
            'high_prob': results.high_prob * 100,
            'high_chosen': results.high_prize_chosen,
            'earnings': results.earnings
        }


page_sequence = [
    ResultsWaitPage,
    PaymentOneResults,
]
