import random

from exp.experiment import Experiment


class PaymentMethod:
    def __init__(self, player_id: int, other_id: int, player_experiment: Experiment, other_experiment: Experiment):
        self.player_id = player_id
        self.other_id = other_id
        self.player_experiment = player_experiment
        self.other_experiment = other_experiment

    def method_one_payment(self):
        results = Results()
        results.player_id = self.player_id
        results.other_id = self.other_id
        phase_one = self.player_experiment.phase_one
        results.phase_one_round = phase_one.random_round()

        results.left_auction = phase_one.left_auction(results.phase_one_round)
        results.right_auction = phase_one.right_auction(results.phase_one_round)

        results.preferred_position = phase_one.preferred_position(results.phase_one_round)
        if results.preferred_position == phase_one.INDIFFERENT:
            results.indifferent_random_value = random.random()
            if results.indifferent_random_value < 0.5:
                results.auction = phase_one.left_auction(results.phase_one_round)
            else:
                results.auction = phase_one.right_auction(results.phase_one_round)
        else:
            results.auction = phase_one.preffered_auction(results.phase_one_round)

        results.random_signal = results.auction.random_signal()
        results.bid = results.auction.bids[results.random_signal]
        results.other_bid = self.other_experiment.auctions[results.auction.aid].bids[results.random_signal]

        if results.bid == results.other_bid:
            results.win_lottery = random.randint(0, 1) == 1
        else:
            results.win_lottery = results.bid > results.other_bid

        results.other_random_signal = results.auction.random_signal()
        if results.win_lottery:
            results.low_prob = results.auction.low_probability(results.random_signal, results.other_random_signal)
            results.high_prob = results.auction.high_probability(results.random_signal, results.other_random_signal)
            results.low_value = results.auction.low_value(results.random_signal, results.other_random_signal)
            results.high_value = results.auction.high_value(results.random_signal, results.other_random_signal)

            results.lottery_random_value = random.random()
            if results.lottery_random_value < results.low_prob:
                results.low_prize_chosen = True
                results.earnings = results.low_value - results.bid
            else:
                results.high_prize_chosen = True
                results.earnings = results.high_value - results.bid

        return results

    def method_two_payment(self):
        results = Results()
        phase_two = self.player_experiment.phase_two
        results.phase_two_round = phase_two.random_round()
        results.phase_two_auction = phase_two.get_auction(results.phase_two_round)
        results.cutoff = results.phase_two_auction.cutoff

        max_value = results.phase_two_auction.max_value
        min_value = results.phase_two_auction.min_value
        results.random_offer = (max_value - min_value) * random.random() + min_value
        if results.random_offer >= results.cutoff:
            return results.random_offer
        else:
            return self.method_one_payment()


class Results:
    def __init__(self):
        self.player_id = -1
        self.other_id = -1
        self.phase_one_round = - 1
        self.preferred_position = - 1
        self.indifferent_random_value = -1
        self.lottery_random_value = -1
        self.auction = None
        self.left_auction = None
        self.right_auction = None
        self.bid = -1
        self.other_bid = -1
        self.low_prize_chosen = False
        self.high_prize_chosen = False
        self.low_value = -1
        self.high_value = -1
        self.low_prob = -1
        self.high_prob = -1
        self.random_signal = -1
        self.other_random_signal = -1
        self.win_lottery = False
        self.earnings = 0
        # type 2
        self.phase_two_round = - 1
        self.phase_two_auction = None
        self.cutoff = -1
        self.random_offer = -1
