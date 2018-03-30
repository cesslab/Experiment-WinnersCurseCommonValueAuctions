class Auction:
    LOW = 0
    HIGH = 1
    VALUE = 0
    PROBABILITY = 1

    def __init__(self, type, kind, matrix=[], signals=[]):
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

    def left_auction(self, round):
        auction_id = self.pairs[round][self.LEFT]
        return self.auctions[auction_id]

    def right_auction(self, round):
        auction_id = self.pairs[round][self.RIGHT]
        return self.auctions[auction_id]


class PhaseTwoAuctionCollection:
    def __init__(self, ids, auctions):
        self.ids = ids
        self.auctions = auctions

    def auction(self, round):
        auction_id = self.ids[round]
        return self.auctions[auction_id]


AUCTIONS = [
    Auction(
        type=1,
        matrix=[[[1], [2]], [[0.2], [0.3]]],
        signals=[1, 5, 7, 8]
    ),
    Auction(
        type=1,
        matrix=[[[1], [2]], [[0.2], [0.3]]],
        signals=[1, 5, 7, 8]
    ),
    Auction(
        type=1,
        matrix=[[[1], [2]], [[0.2], [0.3]]],
        signals=[1, 5, 7, 8]
    ),
    Auction(
        type=1,
        matrix=[[[1], [2]], [[0.2], [0.3]]],
        signals=[1, 5, 7, 8]
    ),
]


class AuctionCollectionFactory:
    @staticmethod
    def phase_one_auctions():
        pairs = [(0, 1), (2, 3)]
        return PhaseOneAuctionCollection(pairs, AUCTIONS)

    def phase_two_auctions():
        ids = [1, 2, 3, 4]
        return PhaseTwoAuctionCollection(ids, AUCTIONS)
