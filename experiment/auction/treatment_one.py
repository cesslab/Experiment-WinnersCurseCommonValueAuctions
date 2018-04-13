from .auctions import Auction

PHASE_ONE_AUCTION_PAIRS = [
    [1, 2], [3, 4]
]

PHASE_TWO_AUCTION_GROUP = [
    {'auction_ids': [1, 2, 3, 4], 'min_max': (7, 28)}
]

PHASE_TWO_AUCTION_EXCLUDE_LIST = [0]

AUCTIONS = [
    # 0
    Auction(
        id=0,
        type=1,
        matrix=[[[10], [20]], [[0.25], [0.75]]],
        signals=[]
    ),
    # a
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

