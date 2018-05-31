import random

from typing import List, Tuple
from exp.auctions import Auction
from exp.phases import (PhaseFour)
from exp.experiment import Experiment
from exp.lottery import Lottery


class MethodOneResults:
    def __init__(self):
        self.player_id: int = -1
        self.other_player_id: int = -1
        self.phase_one_round: int = - 1
        self.preferred_position: int = - 1
        self.indifferent_random_value: float = -1.0
        self.lottery_random_value: float = -1.0
        self.auction: Auction = None
        self.auction_id: int = -1
        self.left_auction: Auction = None
        self.left_auction_id: int = -1
        self.right_auction: Auction = None
        self.right_auction_id: int = -1
        self.bid: float = -1.0
        self.other_bid: float = -1.0
        self.low_prize_chosen: bool = False
        self.high_prize_chosen: bool = False
        self.low_value: int = -1
        self.high_value: int = -1
        self.low_prob: float = -1.0
        self.high_prob: float = -1.0
        self.random_signal: float = -1.0
        self.random_signal_is_percentage: bool = False
        self.other_random_signal: float = -1.0
        self.other_random_signal_is_percentage: bool = False
        self.lottery_won: bool = False
        self.earnings: float = -1.0
        self.realized: float = -1.0

    def save_round(self, round_id: id):
        self.phase_one_round = round_id

    def save_player_ids(self, player_id: id, other_player_id: id):
        self.player_id = player_id
        self.other_player_id = other_player_id

    def save_round_auctions(self, left_auction: Auction, right_auction: Auction, chosen_auction: Auction):
        self.auction = chosen_auction
        self.auction_id = chosen_auction.aid
        self.left_auction = left_auction
        self.left_auction_id = left_auction.aid
        self.right_auction = right_auction
        self.right_auction_id = right_auction.aid

    def save_preferred_position(self, preferred_position: int):
        self.preferred_position = preferred_position

    def save_indifferent_random_value(self, random_val: float):
        self.indifferent_random_value = random_val

    def save_auction_signal(self, signal, is_percentage: bool, other_signal: float, other_is_percentage: float):
        self.random_signal = signal
        self.random_signal_is_percentage = is_percentage
        self.other_random_signal = other_signal
        self.other_random_signal_is_percentage = other_is_percentage

    def save_bids(self, bid, other_bid):
        self.bid = bid
        self.other_bid = other_bid

    def save_lottery_outcome(self, lottery_won):
        self.lottery_won = lottery_won

    def save_lottery_details(self, auction: Auction, random_signal: float, other_random_signal: float):
        self.low_prob = auction.low_probability(random_signal, other_random_signal)
        self.high_prob = auction.high_probability(random_signal, other_random_signal)
        self.low_value = auction.low_value(random_signal, other_random_signal)
        self.high_value = auction.high_value(random_signal, other_random_signal)

    def save_random_lottery_val(self, rand_lottery_val: float):
        self.lottery_random_value = rand_lottery_val

    def save_prize_chosen(self, high_prize_chosen: bool):
        self.high_prize_chosen = high_prize_chosen
        self.low_prize_chosen = not high_prize_chosen

    def save_lottery_realized(self, realized: float):
        self.realized = realized

    def save_earnings(self, earnings: float):
        self.earnings = earnings


class MethodTwoResults:
    def __init__(self):
        self.auction: Auction = None
        self.auction_id: int = -1
        self.cutoff: float = -1.0
        self.random_offer: float = -1.0
        self.player_id: int = -1
        self.other_player_id: int = -1
        self.bid: float = -1.0
        self.other_bid: float = -1.0
        self.low_prize_chosen: bool = False
        self.high_prize_chosen: bool = False
        self.lottery_random_value: float = -1.0
        self.low_value: int = -1
        self.high_value: int = -1
        self.low_prob: float = -1.0
        self.high_prob: float = -1.0
        self.random_signal: float = -1.0
        self.random_signal_is_percentage: bool = False
        self.other_random_signal: float = -1.0
        self.other_random_signal_is_percentage: bool = False
        self.lottery_won: bool = False
        self.earnings: float = -1.0
        self.realized: float = -1.0
        self.phase_two_round: int = - 1
        self.offer_accepted: bool = False

    def save_round(self, round_number):
        self.phase_two_round = round_number

    def save_player_ids(self, player_id: id, other_player_id: id):
        self.player_id = player_id
        self.other_player_id = other_player_id

    def save_auction(self, auction):
        self.auction = auction
        self.auction_id = auction.aid

    def save_cutoff(self, cutoff):
        self.cutoff = cutoff

    def save_random_offer(self, random_offer):
        self.random_offer = random_offer

    def save_earnings(self, earnings):
        self.earnings = earnings

    def save_auction_results(self, won_auction):
        self.offer_accepted = won_auction

    def save_auction_signal(self, signal, is_percentage: bool, other_signal: float, other_is_percentage: float):
        self.random_signal = signal
        self.random_signal_is_percentage = is_percentage
        self.other_random_signal = other_signal
        self.other_random_signal_is_percentage = other_is_percentage

    def save_bids(self, bid, other_bid):
        self.bid = bid
        self.other_bid = other_bid

    def save_lottery_outcome(self, lottery_won):
        self.lottery_won = lottery_won

    def save_lottery_details(self, auction: Auction, random_signal: float, other_random_signal: float):
        self.low_prob = auction.low_probability(random_signal, other_random_signal)
        self.high_prob = auction.high_probability(random_signal, other_random_signal)
        self.low_value = auction.low_value(random_signal, other_random_signal)
        self.high_value = auction.high_value(random_signal, other_random_signal)

    def save_random_lottery_val(self, rand_lottery_val: float):
        self.lottery_random_value = rand_lottery_val

    def save_prize_chosen(self, high_prize_chosen: bool):
        self.high_prize_chosen = high_prize_chosen
        self.low_prize_chosen = not high_prize_chosen

    def save_lottery_realized(self, realized: float):
        self.realized = realized


class MethodThreeResults:
    def __init__(self):
        self.rolled_side: int = -1
        self.bet_color: int = -1
        self.rolled_side_encoded: str = ''
        self.lottery_chosen: int = -1
        self.die_encoding: List[Tuple[str, int]] = None
        self.random_cutoff: float = -1
        self.play_lottery: bool = False
        self.num_red: int = -1
        self.num_blue: int = -1
        self.high_red_chosen: bool = False
        self.high_blue_chosen: bool = False
        self.random_number_red: int = -1
        self.realized_value: int = -1
        self.lottery: Lottery = None
        self.cutoff: float = -1.0
        self.low_value: int = -1
        self.high_value: int = -1
        self.earnings: float = -1.0

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

    def save_phase_three_earnings(self, earnings: float):
        self.earnings = float(earnings)


class PaymentMethod:
    def __init__(self, player_id: int, other_id: int, player_experiment: Experiment, other_experiment: Experiment):
        self.player_id = player_id
        self.other_id = other_id
        self.player_experiment = player_experiment
        self.other_experiment = other_experiment

    def method_one_payment(self, results: MethodOneResults) -> MethodOneResults:
        results.save_player_ids(self.player_id, self.other_id)
        phase = self.player_experiment.phase_one
        random_round = phase.random_round()
        results.save_round(random_round)

        preferred_position = phase.preferred_position(random_round)
        results.save_preferred_position(preferred_position)
        if preferred_position == phase.INDIFFERENT:
            r = random.random()
            results.save_indifferent_random_value(r)
            if r < 0.5:
                auction = phase.left_auction(random_round)
            else:
                auction = phase.right_auction(random_round)
        else:
            auction = phase.preferred_auction(random_round)

        results.save_round_auctions(phase.left_auction(random_round), phase.right_auction(random_round), auction)

        # Selecting a random signal
        random_signal = auction.random_signal()
        signal_percentage = auction.signal_is_percentage
        other_random_signal = auction.random_signal()
        other_signal_percentage = auction.signal_is_percentage
        results.save_auction_signal(random_signal, signal_percentage, other_random_signal, other_signal_percentage)

        bid = auction.bids[random_signal]
        other_bid = self.other_experiment.auctions[auction.aid].bids[random_signal]
        results.save_bids(bid, other_bid)

        if bid == other_bid:
            win_lottery = random.randint(0, 1) == 1
        else:
            win_lottery = bid > other_bid
        results.save_lottery_outcome(win_lottery)

        results.save_lottery_details(auction, random_signal, other_random_signal)

        random_lottery_value = random.random()
        results.save_random_lottery_val(random_lottery_value)

        high_prize_chosen = False
        low_prob = auction.low_probability(random_signal, other_random_signal)
        if random_lottery_value < low_prob:
            realized = auction.low_value(random_signal, other_random_signal)
            earnings = realized - bid
        else:
            high_prize_chosen = True
            realized = auction.high_value(random_signal, other_random_signal)
            earnings = realized - bid

        if not win_lottery:
            earnings = 0

        results.save_prize_chosen(high_prize_chosen)
        results.save_lottery_realized(realized)
        results.save_earnings(earnings)

        return results

    def method_two_payment(self, results: MethodTwoResults) -> MethodTwoResults:
        results.save_player_ids(self.player_id, self.other_id)
        phase_two = self.player_experiment.phase_two
        random_round = phase_two.random_round()
        results.save_round(random_round)

        auction = phase_two.get_auction(random_round)
        results.save_auction(auction)

        cutoff = auction.cutoff
        results.save_cutoff(cutoff)

        max_value = auction.max_value
        min_value = auction.min_value
        random_offer = (max_value - min_value) * random.random() + min_value
        results.save_random_offer(random_offer)

        offer_accepted = False
        if random_offer >= cutoff:
            offer_accepted = True

        results.save_auction_results(offer_accepted)

        if offer_accepted:
            results.save_earnings(random_offer)
            return results

        # Selecting a random signal
        random_signal = auction.random_signal()
        signal_percentage = auction.signal_is_percentage
        other_random_signal = auction.random_signal()
        other_signal_percentage = auction.signal_is_percentage
        results.save_auction_signal(random_signal, signal_percentage, other_random_signal, other_signal_percentage)

        bid = auction.bids[random_signal]
        other_bid = self.other_experiment.auctions[auction.aid].bids[random_signal]
        results.save_bids(bid, other_bid)

        if bid == other_bid:
            win_lottery = random.randint(0, 1) == 1
        else:
            win_lottery = bid > other_bid
        results.save_lottery_outcome(win_lottery)

        results.save_lottery_details(auction, random_signal, other_random_signal)

        random_lottery_value = random.random()
        results.save_random_lottery_val(random_lottery_value)

        high_prize_chosen = False
        low_prob = auction.low_probability(random_signal, other_random_signal)
        if random_lottery_value < low_prob:
            realized = auction.low_value(random_signal, other_random_signal)
            earnings = realized - bid
        else:
            high_prize_chosen = True
            realized = auction.high_value(random_signal, other_random_signal)
            earnings = realized - bid

        if not win_lottery:
            earnings = 0

        results.save_prize_chosen(high_prize_chosen)
        results.save_lottery_realized(realized)
        results.save_earnings(earnings)

        return results

    def method_three_results(self, results: MethodThreeResults) -> MethodThreeResults:
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
