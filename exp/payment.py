import random

from exp.phases import (PhaseOne, PhaseTwo, PhaseThree, PhaseFour)
from exp.experiment import Experiment
from exp.lottery import Lottery


class Results:
    def __init__(self):
        # method 1
        self.player_id = -1
        self.other_player_id = -1
        self.phase_one_round = - 1
        self.preferred_position = - 1
        self.indifferent_random_value = -1
        self.lottery_random_value = -1
        self.auction = None
        self.auction_id = -1
        self.left_auction = None
        self.left_auction_id = -1
        self.right_auction = None
        self.right_auction_id = -1
        self.bid = -1
        self.other_bid = -1
        self.low_prize_chosen = False
        self.high_prize_chosen = False
        self.low_value = -1
        self.high_value = -1
        self.low_prob = -1
        self.high_prob = -1
        self.random_signal = -1
        self.random_signal_is_percentage = False
        self.other_random_signal = -1
        self.other_random_signal_is_percentage = False
        self.win_lottery = False
        self.earnings = -1
        self.realized = -1
        # method 2
        self.phase_two_round = - 1
        self.cutoff_auction = None
        self.cutoff = -1
        self.random_offer = -1
        self.offer_accepted = False
        # method 3
        self.rolled_side = -1
        self.bet_color = -1
        self.rolled_side_encoded = None
        self.total_num = -1
        self.lottery_chosen = -1
        self.die_encoding = None
        self.random_cutoff = -1
        self.play_lottery = False
        self.num_red = -1
        self.num_blue = -1
        self.high_red_chosen = False
        self.high_blue_chosen = False
        self.random_number_red = -1
        self.realized_value = -1
        self.lottery = None

    def save_phase_three_lottery(self, lottery: Lottery):
        self.lottery = lottery
        self.bet_color = lottery.bet
        self.lottery_chosen = lottery.lid
        self.cutoff = lottery.cutoff
        self.high_value = lottery.high_value
        self.low_value = lottery.low_value

    def save_phase_three_die_info(self, phase_four: PhaseFour):
        self.rolled_side = phase_four.die_side
        self.rolled_side_encoded = phase_four.die_side_encoded()
        self.die_encoding = phase_four.die_side_encoding_pairs()

    def save_phase_three_random_cutoff(self, random_cutoff: float):
        self.random_cutoff = random_cutoff

    def save_phase_three_lottery_played(self, play_lottery: bool):
        self.play_lottery = play_lottery

    def save_phase_three_random_number_red(self, random_number_red: float):
        self.random_number_red = random_number_red

    def save_phase_three_num_red_blue(self, num_red: int, num_blue: int):
        self.num_red = num_red
        self.num_blue = num_blue

    def save_phase_three_high_color_chosen(self, high_red_chosen: bool, high_blue_chosen: bool):
        self.high_red_chosen = high_red_chosen
        self.high_blue_chosen = high_blue_chosen

    def save_phase_three_realized_value(self, realized_value: int):
        self.realized_value = realized_value

    def save_phase_three_earnings(self, earnings):
        self.earnings = earnings


class PaymentMethod:
    def __init__(self, player_id: int, other_id: int, player_experiment: Experiment, other_experiment: Experiment):
        self.player_id = player_id
        self.other_id = other_id
        self.player_experiment = player_experiment
        self.other_experiment = other_experiment

    def method_one_payment(self, results: Results) -> Results:
        # Selecting an auction from phase one
        results.player_id = self.player_id
        results.other_player_id = self.other_id
        phase_one = self.player_experiment.phase_one
        results.phase_one_round = phase_one.random_round()

        results.left_auction = phase_one.left_auction(results.phase_one_round)
        results.left_auction_id = results.left_auction.aid
        results.right_auction = phase_one.right_auction(results.phase_one_round)
        results.right_auction_id = results.right_auction.aid

        results.preferred_position = phase_one.preferred_position(results.phase_one_round)
        if results.preferred_position == phase_one.INDIFFERENT:
            results.indifferent_random_value = random.random()
            if results.indifferent_random_value < 0.5:
                results.auction = phase_one.left_auction(results.phase_one_round)
            else:
                results.auction = phase_one.right_auction(results.phase_one_round)
        else:
            results.auction = phase_one.preferred_auction(results.phase_one_round)

        results.auction_id = results.auction.aid

        # Selecting a random signal
        results.random_signal = results.auction.random_signal()
        results.random_signal_is_percentage = results.auction.signal_is_percentage
        results.bid = results.auction.bids[results.random_signal]
        results.other_bid = self.other_experiment.auctions[results.auction.aid].bids[results.random_signal]

        if results.bid == results.other_bid:
            results.win_lottery = random.randint(0, 1) == 1
        else:
            results.win_lottery = results.bid > results.other_bid

        results.other_random_signal = results.auction.random_signal()
        results.other_random_signal_is_percentage = results.auction.signal_is_percentage

        results.low_prob = results.auction.low_probability(results.random_signal, results.other_random_signal)
        results.high_prob = results.auction.high_probability(results.random_signal, results.other_random_signal)
        results.low_value = results.auction.low_value(results.random_signal, results.other_random_signal)
        results.high_value = results.auction.high_value(results.random_signal, results.other_random_signal)

        results.lottery_random_value = random.random()

        if results.lottery_random_value < results.low_prob:
            results.low_prize_chosen = True
            results.realized = results.low_value
        else:
            results.high_prize_chosen = True
            results.realized = results.high_value

        if not results.win_lottery:
            results.earnings = 0
        elif results.low_prize_chosen:
            results.earnings = results.low_value - results.bid
        else:
            results.earnings = results.high_value - results.bid

        return results

    def method_two_payment(self, results: Results) -> Results:
        phase_two = self.player_experiment.phase_two
        results.phase_two_round = phase_two.random_round()
        results.cutoff_auction = phase_two.get_auction(results.phase_two_round)
        results.cutoff = results.cutoff_auction.cutoff

        max_value = results.cutoff_auction.max_value
        min_value = results.cutoff_auction.min_value
        results.random_offer = (max_value - min_value) * random.random() + min_value
        if results.random_offer >= results.cutoff:
            results.offer_accepted = True
            results.earnings = results.random_offer
            return results
        else:
            results.offer_accepted = False

        results.auction = results.cutoff_auction
        results.auction_id = results.auction.aid

        results.random_signal = results.auction.random_signal()
        results.bid = results.auction.bids[results.random_signal]
        results.other_bid = self.other_experiment.auctions[results.auction.aid].bids[results.random_signal]

        if results.bid == results.other_bid:
            results.win_lottery = random.randint(0, 1) == 1
        else:
            results.win_lottery = results.bid > results.other_bid

        results.other_random_signal = results.auction.random_signal()

        results.low_prob = results.auction.low_probability(results.random_signal, results.other_random_signal)
        results.high_prob = results.auction.high_probability(results.random_signal, results.other_random_signal)
        results.low_value = results.auction.low_value(results.random_signal, results.other_random_signal)
        results.high_value = results.auction.high_value(results.random_signal, results.other_random_signal)

        results.lottery_random_value = random.random()

        if results.lottery_random_value < results.low_prob:
            results.low_prize_chosen = True
            results.realized = results.low_value
        else:
            results.high_prize_chosen = True
            results.realized = results.high_value

        if not results.win_lottery:
            results.earnings = 0
        elif results.low_prize_chosen:
            results.earnings = results.low_value - results.bid
        else:
            results.earnings = results.high_value - results.bid

        return results

    def method_three_results(self, results: Results) -> Results:
        phase_four = self.player_experiment.phase_four
        lottery = phase_four.chosen_lottery()
        random_cutoff = random.randint(lottery.min_cutoff, lottery.max_cutoff)

        results.save_phase_three_lottery(lottery)
        results.save_phase_three_die_info(phase_four)
        results.save_phase_three_random_cutoff(random_cutoff)

        if random_cutoff < lottery.cutoff:
            play_lottery = True
        else:
            results.save_phase_three_earnings(random_cutoff)
            play_lottery = False
        results.save_phase_three_lottery_played(play_lottery)

        random_number_red = random.randint(0, lottery.total)
        results.save_phase_three_random_number_red(random_number_red)

        high_red_chosen = False
        if lottery.ltype == Lottery.ALL_KNOWN:
            num_red = lottery.number_red
            if random_number_red <= num_red:
                high_red_chosen = True
        elif lottery.ltype == Lottery.COMPOUND_RISK:
            num_red = random.randint(0, lottery.total)
            if random_number_red <= num_red:
                high_red_chosen = True
        else:
            num_red = lottery.number_red
            if random_number_red <= num_red:
                high_red_chosen = True

        results.save_phase_three_num_red_blue(num_red, lottery.total - num_red)
        results.save_phase_three_high_color_chosen(high_red_chosen, not high_red_chosen)

        if high_red_chosen and lottery.bet == Lottery.BET_HIGH_RED:
            realized_value = lottery.high_value
        else:
            realized_value = lottery.low_value

        results.save_phase_three_realized_value(realized_value)

        if play_lottery:
            results.save_phase_three_earnings(realized_value)

        return results
