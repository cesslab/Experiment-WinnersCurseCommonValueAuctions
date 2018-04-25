from typing import List
import random


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
        self.cutoff = None
        self.bids = {}
        self.random_signal = random.choice(signals)

        for signal in signals:
            self.bids[signal] = None

    @property
    def low_values(self):
        return self.matrix[Auction.VALUE][Auction.LOW]

    @property
    def high_values(self):
        return self.matrix[Auction.VALUE][Auction.HIGH]

    @property
    def low_probabilities(self):
        return self.matrix[Auction.PROBABILITY][Auction.LOW]

    @property
    def high_probabilities(self):
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
            return (self.low_values[Auction.LOW] + signal) / 2
        elif self.atype == 3:
            return (self.high_values[Auction.LOW] + signal) / 2
        elif self.atype == 4:
            return (self.high_probabilities[Auction.LOW] + signal) / 2
        else:
            return (self.low_probabilities[Auction.LOW] + signal) / 2

    def high_update(self, signal):
        if self.atype == 2:
            return (self.low_values[Auction.HIGH] + signal) / 2
        if self.atype == 3:
            return (self.high_values[Auction.HIGH] + signal) / 2
        if self.atype == 4:
            return (self.high_probabilities[Auction.HIGH] + signal) / 2
        if self.atype == 5:
            return (self.low_probabilities[Auction.HIGH] + signal) / 2

    def low_value(self, player_signal, other_signal):
        if self.atype == 2:
            return (player_signal + other_signal) / 2
        else:
            return self.low_values[0]

    def high_value(self, player_signal, other_signal):
        if self.atype == 3:
            return (player_signal + other_signal) / 2
        else:
            return self.high_values[0]

    def low_probability(self, player_signal, other_signal):
        if self.atype == 5:
            return (player_signal + other_signal) / 2
        elif self.atype == 4:
            return 1 - (player_signal + other_signal) / 2
        else:
            return self.low_probabilities[0]

    def high_probability(self, player_signal, other_signal):
        if self.atype == 4:
            return (player_signal + other_signal) / 2
        elif self.atype == 5:
            return 1 - (player_signal + other_signal) / 2
        else:
            return self.high_probabilities[0]

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
