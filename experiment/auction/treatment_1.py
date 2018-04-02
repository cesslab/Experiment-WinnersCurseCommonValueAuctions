from .auctions import Auction, PhaseOneAuctionCollection, PhaseTwoAuctionCollection

AUCTIONS = [
    # 0
    Auction(
        type=1,
        matrix=[[[10], [20]], [[0.25], [0.75]]],
        signals=[]
    ),
    # 1
    Auction(
        type=2,
        matrix=[[[7, 13], [25]], [[0.25], [0.75]]],
        signals=[7, 8, 10, 12, 13]
    ),
    # 2
    Auction(
        type=4,
        matrix=[[[10], [25]], [[0.1, 0.4], []]],
        signals=[0.1, 0.15, 0.25, 0.35, 0.4]
    ),
    # 3
    Auction(
        type=3,
        matrix=[[[10], [46, 64]], [[0.25], [0.75]]],
        signals=[46, 49, 55, 61, 64]
    ),
    # 4
    Auction(
        type=5,
        matrix=[[[10], [55]], [[], [0.6, 0.9]]],
        signals=[0.6, 0.65, 0.75, 0.85, 0.9]
    ),
    # ---------------------------------------------
    # 5
    # ---------------------------------------------
]


class AuctionCollectionFactory:
    @staticmethod
    def phase_one_auctions():
        pairs = [(1, 2), (3, 4)]
        return PhaseOneAuctionCollection(pairs, AUCTIONS)

    @staticmethod
    def phase_two_auctions():
        ids = [1, 2, 3, 4]
        min_max = [{'auction_ids': [1, 2, 3, 4], 'min_max': (7, 28)}]
        return PhaseTwoAuctionCollection(ids, min_max, AUCTIONS)
