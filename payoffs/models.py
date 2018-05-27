from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

from exp.payment import Results

author = 'Anwar A. Ruff'

doc = """
Phase 4: Payoff determination
https://github.com/cesslab/Experiment-WinnersCurseCommonValueAuctions
"""


class Constants(BaseConstants):
    name_in_url = 'payoffs'
    players_per_group = None
    num_rounds = 1
    # -------------------------
    # Game Constants
    # -------------------------
    Endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 1 - Stage 1 & 3
    method_1_player_id = models.IntegerField()
    method_1_other_player_id = models.IntegerField()
    method_1_phase_one_round = models.IntegerField()
    method_1_preferred_position = models.IntegerField()
    method_1_indifferent_random = models.DecimalField(max_digits=4, decimal_places=2)
    method_1_auction = models.IntegerField()
    method_1_left_auction = models.IntegerField()
    method_1_right_auction = models.IntegerField()
    method_1_bid = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_other_bid = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_win_lottery = models.BooleanField()
    method_1_low_chosen = models.BooleanField()
    method_1_high_chosen = models.BooleanField()
    method_1_low_value = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_high_value = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_low_prob = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_high_prob = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_signal = models.DecimalField(max_digits=4, decimal_places=2)
    method_1_others_signal = models.DecimalField(max_digits=4, decimal_places=2)
    method_1_realized_value = models.DecimalField(max_digits=6, decimal_places=2)
    method_1_earnings = models.DecimalField(max_digits=4, decimal_places=2)

    method_2_player_id = models.IntegerField()
    method_2_other_player_id = models.IntegerField()
    method_2_auction = models.IntegerField()
    method_2_price = models.DecimalField(max_digits=4, decimal_places=2)
    method_2_random_price = models.DecimalField(max_digits=4, decimal_places=2)
    method_2_price_accepted = models.BooleanField()
    method_2_bid = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_other_bid = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_win_lottery = models.BooleanField()
    method_2_low_chosen = models.BooleanField()
    method_2_high_chosen = models.BooleanField()
    method_2_low_value = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_high_value = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_low_prob = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_high_prob = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_signal = models.DecimalField(max_digits=4, decimal_places=2)
    method_2_others_signal = models.DecimalField(max_digits=4, decimal_places=2)
    method_2_realized_value = models.DecimalField(max_digits=6, decimal_places=2)
    method_2_earnings = models.DecimalField(max_digits=4, decimal_places=2)

    method_3_die_side = models.IntegerField()
    method_3_lottery_id = models.IntegerField()
    method_3_random_price = models.DecimalField(max_digits=4, decimal_places=2)
    method_3_lottery_played = models.BooleanField()
    method_3_blue_chosen = models.BooleanField()
    method_3_red_chosen = models.BooleanField()
    method_3_num_red = models.IntegerField()
    method_3_num_blue = models.IntegerField()
    method_3_earnings = models.DecimalField(max_digits=4, decimal_places=2)
    method_3_random_chip_id = models.DecimalField(max_digits=4, decimal_places=2)
    method_3_realized_value = models.DecimalField(max_digits=4, decimal_places=2)
    # Red = 0, Blue = 1
    method_3_bet_color = models.IntegerField()

    def save_results(self, method_1: Results, method_2: Results, method_3: Results):
        self.method_1_player_id = method_1.player_id
        self.method_1_other_player_id = method_1.other_player_id
        self.method_1_phase_one_round = method_1.phase_one_round
        self.method_1_preferred_position = method_1.preferred_position
        self.method_1_indifferent_random = method_1.indifferent_random_value
        self.method_1_auction = method_1.auction_id
        self.method_1_left_auction = method_1.left_auction_id
        self.method_1_right_auction = method_1.right_auction_id
        self.method_1_bid = method_1.bid
        self.method_1_other_bid = method_1.other_bid
        self.method_1_win_lottery = method_1.win_lottery
        self.method_1_low_chosen = method_1.low_prize_chosen
        self.method_1_high_chosen = method_1.high_prize_chosen
        self.method_1_low_value = method_1.low_value
        self.method_1_high_value = method_1.high_value
        self.method_1_low_prob = method_1.low_prob
        self.method_1_high_prob = method_1.high_prob
        self.method_1_signal = method_1.random_signal
        self.method_1_others_signal = method_1.other_random_signal
        self.method_1_realized_value = method_1.realized
        self.method_1_earnings = method_1.earnings

        self.method_2_player_id = method_2.player_id
        self.method_2_other_player_id = method_2.other_player_id
        self.method_2_auction = method_2.auction_id
        self.method_2_price = method_2.cutoff
        self.method_2_random_price = method_2.random_offer
        self.method_2_price_accepted = method_2.offer_accepted
        self.method_2_bid = method_2.bid
        self.method_2_other_bid = method_2.other_bid
        self.method_2_win_lottery = method_2.win_lottery
        self.method_2_low_chosen = method_2.low_prize_chosen
        self.method_2_high_chosen = method_2.high_prize_chosen
        self.method_2_low_value = method_2.low_value
        self.method_2_high_value = method_2.high_value
        self.method_2_low_prob = method_2.low_prob
        self.method_2_high_prob = method_2.high_prob
        self.method_2_signal = method_2.random_signal
        self.method_2_others_signal = method_2.other_random_signal
        self.method_2_realized_value = method_2.realized
        self.method_2_earnings = method_2.earnings

        self.method_3_die_side = method_3.rolled_side
        self.method_3_lottery_id = method_3.lottery_chosen
        self.method_3_bet_color = method_3.bet_color
        self.method_3_random_price = method_3.random_cutoff
        self.method_3_lottery_played = method_3.play_lottery
        self.method_3_random_chip_id = method_3.random_number_red
        self.method_3_num_red = method_3.num_red
        self.method_3_num_blue = method_3.num_blue
        self.method_3_blue_chosen = method_3.high_blue_chosen
        self.method_3_red_chosen = method_3.high_red_chosen
        self.method_3_realized_value = method_3.realized_value
        self.method_3_earnings = method_3.earnings
