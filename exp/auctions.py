from typing import List, Dict
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
        self.signal_is_percentage = (atype == 4 or atype == 5)
        self.min_max = min_max
        self.cutoff = None
        self.bids = {}

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

    def random_signal(self):
        return random.choice(self.signals)

    def range_low(self):
        assert (2 <= self.atype <= 5)
        if self.atype == 2:
            return self.low_values[Auction.LOW]
        elif self.atype == 3:
            return self.high_values[Auction.LOW]
        elif self.atype == 4:
            return self.high_probabilities[Auction.LOW]
        else:
            return self.low_probabilities[Auction.LOW]

    def range_high(self):
        assert (2 <= self.atype <= 5)
        if self.atype == 2:
            return self.low_values[Auction.HIGH]
        elif self.atype == 3:
            return self.high_values[Auction.HIGH]
        elif self.atype == 4:
            return self.high_probabilities[Auction.HIGH]
        else:
            return self.low_probabilities[Auction.HIGH]

    def low_update(self, signal) -> float:
        return (self.range_low() + signal) / 2.0

    def high_update(self, signal) -> float:
        return (self.range_high() + signal) / 2.0

    def low_value(self, player_signal, other_signal) -> float:
        if self.atype == 2:
            return (player_signal + other_signal) / 2.0
        else:
            return float(self.low_values[0])

    def high_value(self, player_signal, other_signal):
        if self.atype == 3:
            return (player_signal + other_signal) / 2.0
        else:
            return float(self.high_values[0])

    def low_probability(self, player_signal, other_signal):
        if self.atype == 5:
            return (player_signal + other_signal) / 2.0
        elif self.atype == 4:
            return 1 - (player_signal + other_signal) / 2.0
        else:
            return float(self.low_probabilities[0])

    def high_probability(self, player_signal, other_signal):
        if self.atype == 4:
            return (player_signal + other_signal) / 2.0
        elif self.atype == 5:
            return 1 - (player_signal + other_signal) / 2.0
        else:
            return float(self.high_probabilities[0])

    def get_bid(self, signal):
        assert signal in self.signals
        return self.bids[signal]

    def __str__(self):
        return 'Auction ' % self.aid

    def __rpr__(self):
        return "Auction: {}, Type: {}".format(self.aid, self.atype)


class AuctionFactory:

    @staticmethod
    def auctions(auction_params: Dict) -> Dict[int, Auction]:
        auctions = {}
        for aid, params in auction_params.items():
            auctions[aid] = Auction(
                aid=params['id'],
                atype=params['type'],
                matrix=params['matrix'],
                signals=params['signals'],
                min_max=params['min_max'],
            )
        return auctions

