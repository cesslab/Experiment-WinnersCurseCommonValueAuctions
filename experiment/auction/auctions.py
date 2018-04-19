from typing import List


class Auction:
    LOW = 0
    HIGH = 1
    MIN = 0
    MAX = 1
    VALUE = 0
    PROBABILITY = 1

    def __init__(self, aid: int, atype: int, matrix: List = [], signals: List = [], min_max: List = []):
        self.aid = aid
        self.atype = atype
        self.matrix = matrix
        self.signals = signals
        self.min_max = min_max

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

    @property
    def min_value(self):
        return self.min_max[Auction.MIN]

    @property
    def max_value(self):
        return self.min_max[Auction.MAX]

    def low_update(self, signal):
        assert (2 <= self.atype <= 5)
        if self.atype == 2:
            return (self.val_low[Auction.LOW] + signal) / 2
        elif self.atype == 3:
            return (self.val_high[Auction.LOW] + signal) / 2
        elif self.atype == 4:
            return (self.prob_high[Auction.LOW] + signal) / 2
        else:
            return (self.prob_low[Auction.LOW] + signal) / 2

    def high_update(self, signal):
        if self.atype == 2:
            return (self.val_low[Auction.HIGH] + signal) / 2
        if self.atype == 3:
            return (self.val_high[Auction.HIGH] + signal) / 2
        if self.atype == 4:
            return (self.prob_high[Auction.HIGH] + signal) / 2
        if self.atype == 5:
            return (self.prob_low[Auction.HIGH] + signal) / 2

    def __str__(self):
        return 'Auction ' % self.aid

    def __rpr__(self):
        return "Auction: {}, Type: {}".format(self.aid, self.atype)


class PhaseOneAuctionCollection:
    def __init__(self, left_auctions, right_auctions, auctions):
        self.left_auctions = left_auctions
        self.right_auctions = right_auctions
        self.auctions = auctions

    def left_auction(self, session_round):
        return self.left_auctions[session_round - 1]

    def right_auction(self, session_round):
        return self.right_auctions[session_round - 1]


class PhaseTwoAuctionCollection:
    def __init__(self, auctions):
        self.auctions = auctions

    def auction(self, session_round):
        return self.auctions[session_round - 1]


class PhaseThreeAuctionCollection:
    def __init__(self, auction_signal_pairs):
        self.auction_signal_pairs = auction_signal_pairs

    def auction(self, session_round):
        return self.auction_signal_pairs[session_round - 1]['auction']

    def signal(self, session_round):
        return self.auction_signal_pairs[session_round - 1]['signal']
