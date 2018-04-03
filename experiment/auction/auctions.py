class Auction:
    LOW = 0
    HIGH = 1
    VALUE = 0
    PROBABILITY = 1

    def __init__(self, id, type, matrix=[], signals=[]):
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


class PhaseOneAuctionCollection:
    def __init__(self, left_auctions, right_auctions):
        self.left_auctions = left_auctions
        self.right_auctions = right_auctions

    def left_auction(self, session_round):
        assert(0 < session_round <= len(self.left_auctions))
        return self.left_auctions[session_round - 1]

    def right_auction(self, session_round):
        assert(0 < session_round <= len(self.right_auctions))
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

