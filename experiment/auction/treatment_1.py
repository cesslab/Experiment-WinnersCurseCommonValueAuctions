from .auctions import (
    Auction, PhaseOneAuctionCollection, PhaseTwoAuctionCollection,
    PhaseThreeAuctionCollection)

AUCTIONS = [
    # 0
    Auction(
        id=0,
        type=1,
        matrix=[[[10], [20]], [[0.25], [0.75]]],
        signals=[]
    ),
    # 1
    Auction(
        id=1,
        type=2,
        matrix=[[[7, 13], [25]], [[0.25], [0.75]]],
        signals=[7, 8, 10, 12, 13]
    ),
    # 2
    Auction(
        id=2,
        type=4,
        matrix=[[[10], [25]], [[0.1, 0.4], []]],
        signals=[0.1, 0.15, 0.25, 0.35, 0.4]
    ),
    # 3
    Auction(
        id=3,
        type=3,
        matrix=[[[10], [46, 64]], [[0.25], [0.75]]],
        signals=[46, 49, 55, 61, 64]
    ),
    # 4
    Auction(
        id=4,
        type=5,
        matrix=[[[10], [55]], [[], [0.6, 0.9]]],
        signals=[0.6, 0.65, 0.75, 0.85, 0.9]
    ),
    # ---------------------------------------------
    # 5
    # ---------------------------------------------
]


class AuctionCollectionFactory:
    LEFT_AUCTION = 0

    RIGHT_AUCTION = 1

    PAIRS = [
        (1, 2), (3, 4)
    ]

    PHASE_TWO_AUCTION_EXCLUDE_LIST = [0]

    MIN_MAX = [
        {'auction_ids': [1, 2, 3, 4], 'min_max': (7, 28)}
    ]

    @classmethod
    def phase_one_rounds(cls):
        return len(cls.PAIRS)

    @classmethod
    def phase_two_rounds(cls):
        return len(AUCTIONS) - len(cls.PHASE_TWO_AUCTION_EXCLUDE_LIST)

    @classmethod
    def phase_three_rounds(cls):
        rounds = 0
        for auction in AUCTIONS:
            rounds += len(auction.signals)

        return rounds

    @classmethod
    def phase_one_auctions(cls):
        left_auctions = []
        right_auctions = []
        for pair in cls.PAIRS:
            left_auctions.append(AUCTIONS[pair[cls.LEFT_AUCTION]])
            right_auctions.append(AUCTIONS[pair[cls.RIGHT_AUCTION]])

        return PhaseOneAuctionCollection(left_auctions, right_auctions)

    @classmethod
    def phase_two_auctions(cls):
        auctions = []
        min_max_values = []
        for group in AuctionCollectionFactory.MIN_MAX:
            for auction_id in group['auction_ids']:
                auctions.append(AUCTIONS[auction_id])
                min_max_values.append(group['min_max'])

        return PhaseTwoAuctionCollection(auctions, min_max_values)

    @staticmethod
    def phase_three_auctions():
        auctions = []
        signals = []
        for auction in AUCTIONS:
            for signal in auction.signals:
                auctions.append(auction)
                signals.append(signal)
        return PhaseThreeAuctionCollection(auctions, signals)
