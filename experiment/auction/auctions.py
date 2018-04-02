class Auction:
    LOW = 0
    HIGH = 1
    VALUE = 0
    PROBABILITY = 1

    def __init__(self, type, matrix=[], signals=[]):
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


class PhaseOneAuctionCollection:
    LEFT = 0
    RIGHT = 1

    def __init__(self, pairs, auctions):
        self.pairs = pairs
        self.auctions = auctions

    def left_auction(self, session_round):
        auction_id = self.pairs[session_round - 1][self.LEFT]
        return self.auctions[auction_id]

    def right_auction(self, session_round):
        auction_id = self.pairs[session_round - 1][self.RIGHT]
        return self.auctions[auction_id]


class PhaseTwoAuctionCollection:
    def __init__(self, ids, rages, auctions):
        self.ids = ids
        self.ranges = rages
        self.auctions = auctions

    def auction(self, session_round):
        auction_id = self.ids[session_round - 1]
        return self.auctions[auction_id]

    def auction_min_max(self, session_round):
        for r in self.ranges:
            if self.ids[session_round - 1] in r['auction_ids']:
                return r['min_max']


