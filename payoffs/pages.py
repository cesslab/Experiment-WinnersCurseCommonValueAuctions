from ._builtin import Page, WaitPage

import random
from core.util import Participant
from core.payment import PaymentMethod, MethodThreeResults, MethodOneResults, MethodTwoResults
from core.lottery import Lottery


class FinalPayoffResults(Page):
    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        method_one = Participant.get_payment_one_results(self.player)
        method_two = Participant.get_payment_two_results(self.player)
        method_three = Participant.get_payment_three_results(self.player)
        part_one_earnings = method_one.earnings + method_two.earnings
        part_one_payoff = experiment.PART_ONE_WEIGHT*part_one_earnings*experiment.CONVERSION_RATE
        part_two_payoff = experiment.PART_TWO_WEIGHT*method_three.earnings*experiment.CONVERSION_RATE
        final_payoff = experiment.SHOW_UP_FEE + experiment.ENDOWMENT + part_one_payoff + part_two_payoff
        return {
            'show_up_fee': experiment.SHOW_UP_FEE,
            'endowment': experiment.ENDOWMENT,
            'rate': experiment.CONVERSION_RATE,
            'method_1': round(method_one.earnings, 2),
            'method_2': round(method_two.earnings, 2),
            'method_3': round(method_three.earnings, 2),
            'total_in_credits': round(part_one_earnings, 2),
            'earnings_1': round(part_one_payoff, 2),
            'earnings_2': round(part_two_payoff, 2),
            'final_payoff': round(final_payoff, 2),
        }


class MethodOneResultsPage(Page):
    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        results = Participant.get_payment_one_results(self.player)

        random_position = 'Left' if results.left_auction.aid == results.auction.aid else 'Right'

        if results.preferred_position == experiment.phase_one.LEFT:
            preferred_position = 'Left'
        elif results.preferred_position == experiment.phase_one.RIGHT:
            preferred_position = 'Right'
        else:
            preferred_position = 'Indifferent'

        if results.random_signal_is_percentage:
            random_signal = round(results.random_signal * 100, 2)
        else:
            random_signal = results.random_signal

        if results.other_random_signal_is_percentage:
            others_random_signal = round(results.other_random_signal * 100, 2)
        else:
            others_random_signal = results.other_random_signal
        return {
            'player_id': results.player_id,
            'other_id': results.other_player_id,
            'preferred_position': preferred_position,
            'left_auction': results.left_auction,
            'right_auction': results.right_auction,
            'auction': results.auction,
            'random_position': random_position,
            'bid': results.bid,
            'others_bid': results.other_bid,
            'winner': results.lottery_won,
            'signal_is_percentage': results.random_signal_is_percentage,
            'signal': random_signal,
            'others_signal': others_random_signal,
            'others_signal_is_percentage': results.other_random_signal_is_percentage,
            'low_value': results.low_value,
            'high_value': results.high_value,
            'low_prob': round(results.low_prob * 100, 2),
            'high_prob': round(results.high_prob * 100, 2),
            'high_chosen': results.high_prize_chosen,
            'earnings': results.earnings,
            'realized': results.realized,
            'auction_type': results.auction.atype,
            'low_prize_chosen': results.low_prize_chosen,
            'high_prize_chosen': results.high_prize_chosen,
        }


class MethodTwoResultsPage(Page):
    def vars_for_template(self):
        results = Participant.get_payment_two_results(self.player)

        context = {
            'player_id': results.player_id,
            'other_id': results.other_player_id,
            'cutoff_auction': results.auction,
            'cutoff': results.cutoff,
            'random_offer': round(results.random_offer, 2),
            'offer_accepted': results.offer_accepted,
        }

        if not results.offer_accepted:
            if results.random_signal_is_percentage:
                random_signal = round(results.random_signal * 100, 2)
            else:
                random_signal = int(results.random_signal)

            if results.other_random_signal_is_percentage:
                others_random_signal = round(results.other_random_signal * 100, 2)
            else:
                others_random_signal = int(results.other_random_signal)

            context.update({
                'auction': results.auction,
                'bid': results.bid,
                'others_bid': results.other_bid,
                'winner': results.lottery_won,
                'signal': random_signal,
                'others_signal': others_random_signal,
                'signal_is_percentage': results.random_signal_is_percentage,
                'others_signal_is_percentage': results.other_random_signal_is_percentage,
                'low_value': results.low_value,
                'high_value': results.high_value,
                'low_prob': results.low_prob * 100,
                'high_prob': results.high_prob * 100,
                'high_chosen': results.high_prize_chosen,
                'earnings': results.earnings,
                'realized': results.realized,
                'auction_type': results.auction.atype,
                'low_prize_chosen': results.low_prize_chosen,
                'high_prize_chosen': results.high_prize_chosen,
            })

        return context


class MethodThreeResultsPage(Page):
    def vars_for_template(self):
        results = Participant.get_payment_three_results(self.player)

        context = {
            'rolled_side': results.rolled_side,
            'rolled_side_encoded': results.rolled_side_encoded,
            'die_encoding': results.die_encoding,
            'bet_color': Lottery.BET_HIGH_RED if results.bet_color == Lottery.BET_HIGH_RED else Lottery.BET_HIGH_BLUE,
            'bet_high_red': Lottery.BET_HIGH_RED,
            'bet_high_blue': Lottery.BET_HIGH_BLUE,
            'high_value': results.high_value,
            'low_value': results.low_value,
            'lottery': results.lottery,
            'lottery_type': results.lottery.ltype,
            'cutoff': results.cutoff,
            'random_cutoff': results.random_cutoff,
            'play_lottery': results.play_lottery,
            'num_red': results.num_red,
            'num_blue': results.num_blue,
            'realized_value': results.realized_value,
            'earnings': results.earnings
        }

        return context


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        players = self.group.get_players()[:]
        for i, player in enumerate(players):
            player_id = player.participant.id_in_session
            others = players[:i] + players[i + 1:]
            other_player = random.choice(others)
            other_id = other_player.participant.id_in_session
            experiment = Participant.get_experiment(player)
            other_experiment = Participant.get_experiment(other_player)
            payment_method = PaymentMethod(player_id, other_id, experiment, other_experiment)

            method_one_results = payment_method.method_one_payment(MethodOneResults())
            method_two_results = payment_method.method_two_payment(MethodTwoResults())
            method_three_results = payment_method.method_three_results(MethodThreeResults())
            Participant.set_payment_one_results(player, method_one_results)
            Participant.set_payment_two_results(player, method_two_results)
            Participant.set_payment_three_results(player, method_three_results)

            part_one_earnings = method_one_results.earnings + method_two_results.earnings
            part_one_payoff = experiment.PART_ONE_WEIGHT*part_one_earnings*experiment.CONVERSION_RATE
            part_two_payoff = experiment.PART_TWO_WEIGHT*method_three_results.earnings*experiment.CONVERSION_RATE
            final_payoff = experiment.SHOW_UP_FEE + experiment.ENDOWMENT + part_one_payoff + part_two_payoff
            player.payoff = final_payoff
            player.save_results(method_one_results, method_two_results, method_three_results)


page_sequence = [
    ResultsWaitPage,
    MethodOneResultsPage,
    MethodTwoResultsPage,
    MethodThreeResultsPage,
    FinalPayoffResults
]
