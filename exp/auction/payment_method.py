import random

from exp.auctions import Auction
from exp.phases import PhaseOne, PhaseThree
from exp.experiment import Experiment


class PaymentMethod:
    def __init__(self, player_experiment: Experiment, other_experiment: Experiment):
        self.player_experiment = player_experiment
        self.other_experiment = other_experiment

    def method_one_payment(self):
        results = MethodOneResults()
        results.round_number = self.player_experiment.phase_one.random_round()

        results.left_auction = self.player_experiment.phase_one.left_auction(results.round_number)
        results.right_auction = self.player_experiment.phase_one.right_auction(results.round_number)

        results.preferred_position = self.player_experiment.phase_one.preferred_position(results.round_number)
        if results.preferred_position == self.player_experiment.phase_one.INDIFFERENT:
            results.random_val = random.random()
            if results.random_val < 0.5:
                results.auction = self.player_experiment.phase_one.left_auction(results.round_number)
            else:
                results.auction = self.player_experiment.phase_one.right_auction(results.round_number)
        else:
            results.auction = self.player_experiment.phase_one.preffered_auction(results.round_number)

        results.random_signal = results.auction.random_signal()
        results.bid = results.auction.bids[results.random_signal]








class MethodOneResults:
    def __init__(self):
        self.round_number = - 1
        self.preferred_position = - 1
        self.random_value = -1
        self.auction = None
        self.left_auction = None
        self.right_auction = None
        self.bid = -1
        self.other_bid = -1
        self.random_signal = -1
