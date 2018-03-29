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


class AuctionCollection:
    LEFT = 0
    RIGHT = 1

    def __init__(self, auction_collection):
        self.auction_collection = auction_collection

    def left_auction(self, round):
        return self.auction_collection[round - 1][AuctionCollection.LEFT]

    def right_auction(self, round):
        return self.auction_collection[round - 1][AuctionCollection.RIGHT]


class Treatment:
    @staticmethod
    def t1_auction_collection():
        return AuctionCollection([
            # Pair 1
            [
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
            ],

            # Pair 2
            [
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
            ],
        ])
