import random

from exp.auction import Auction


class PaymentMethodOne:
    INDIFFERENT = 0

    def __init__(self, phase_one_round: int = 0):
        self.phase_one_round = phase_one_round
        self.selected_auction = None
        self.selected_signal = None
        self.left_auction = None
        self.right_auction = None
        self.phase_one_random = -1

    def get_selected_side(self) -> str:
        return 'Left' if self.left_auction.aid == self.selected_auction.aid else 'Right'

    def is_phase_one_payment_round(self, current_round: int) -> bool:
        return current_round == self.phase_one_round

    def set_phase_one_auctions(self, left_auction: Auction, right_auction: Auction, selected_auction_id: int):
        self.left_auction = left_auction
        self.right_auction = right_auction
        if selected_auction_id == PaymentMethodOne.INDIFFERENT:
            self.phase_one_random = random.random()
            if self.phase_one_random < 0.5:
                self.selected_auction = left_auction
            else:
                self.selected_auction = right_auction
        else:
            if selected_auction_id == left_auction.aid:
                self.selected_auction = left_auction
            else:
                self.selected_auction = right_auction


class PaymentMethodTwo(PaymentMethodOne):
    def __init__(self, phase_one_round: int = 0, phase_two_round: int = 0):
        super().__init__(phase_one_round)
        self.phase_two_round = phase_two_round

