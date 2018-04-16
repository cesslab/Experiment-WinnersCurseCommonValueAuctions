from typing import List


class Auction:
    LOW = 0
    HIGH = 1
    VALUE = 0
    PROBABILITY = 1

    def __init__(self, id: int, type: int, matrix: List = [], signals: List = []):
        self.id = id
        self.type = type
        self.matrix = matrix
        self.signals = signals

    @property
    def val_low(self):
        return self.matrix[Auction.VALUE][Auction.LOW]

    @property
    def val_high(self):
        return self.matrix[Auction.VALUE][Auction.HIGH]

    @property
    def prob_low(self):
        return self.matrix[Auction.PROBABILITY][Auction.LOW]

    @property
    def prob_high(self):
        return self.matrix[Auction.PROBABILITY][Auction.HIGH]

    def low_update(self, signal):
        assert (1 <= self.type <= 5)
        if self.type == 2:
            return (self.val_low[Auction.LOW] + signal) / 2
        elif self.type == 3:
            return (self.val_high[Auction.LOW] + signal) / 2
        elif self.type == 4:
            return (self.prob_low[Auction.LOW] + signal) / 2
        else:
            return (self.prob_high[Auction.LOW] + signal) / 2

    def high_update(self, signal):
        if self.type == 2:
            return (self.val_low[Auction.HIGH] + signal) / 2
        if self.type == 3:
            return (self.val_high[Auction.HIGH] + signal) / 2
        if self.type == 4:
            return (self.prob_low[Auction.HIGH] + signal) / 2
        if self.type == 5:
            return (self.prob_high[Auction.HIGH] + signal) / 2

    def __str__(self):
        return 'Auction ' % self.id


class PhaseOneAuctionCollection:
    def __init__(self, left_auctions, right_auctions):
        self.left_auctions = left_auctions
        self.right_auctions = right_auctions

    def left_auction(self, session_round):
        return self.left_auctions[session_round - 1]

    def right_auction(self, session_round):
        return self.right_auctions[session_round - 1]


class PhaseTwoAuctionCollection:
    def __init__(self, auctions, min_max_values):
        self.auctions = auctions
        self.min_max_values = min_max_values

    def auction(self, session_round):
        return self.auctions[session_round - 1]

    def auction_min_max(self, session_round):
        return self.min_max_values[session_round - 1]


class PhaseThreeAuctionCollection:
    def __init__(self, auctions, signals):
        self.signals = signals
        self.auctions = auctions

    def auction(self, session_round):
        return self.auctions[session_round - 1]

    def signal(self, session_round):
        return self.signals[session_round - 1]
