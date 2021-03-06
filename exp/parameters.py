PHASE_ONE_AUCTION_PAIRS = [
    [12, 14],
    [13, 15],
    [22, 24],
    [23, 25],
    [32, 34],
    [33, 35],
    # consistency check
    [12, 24],
    [15, 23],
]

AUCTIONS = {
    12: {
        'id': 12,
        'type': 2,
        'matrix': [[[7, 13], [25]], [[0.75], [0.25]]],
        'signals': [7, 10, 13],
        'min_max': [0, 28],
    },
    13: {
        'id': 13,
        'type': 3,
        'matrix': [[[10], [22, 28]], [[0.25], [0.75]]],
        'signals': [22, 25, 28],
        'min_max': [0, 28],
    },
    14: {
        'id': 14,
        'type': 4,
        'matrix': [[[10], [25]], [[], [0.1, 0.4]]],
        'signals': [0.1, 0.25, 0.4],
        'min_max': [0, 28],
    },
    15: {
        'id': 15,
        'type': 4,
        'matrix': [[[10], [25]], [[], [0.6, 0.9]]],
        'signals': [0.6, 0.75, 0.9],
        'min_max': [0, 28],
    },
    22: {
        'id': 22,
        'type': 2,
        'matrix': [[[1, 19], [55]], [[0.75], [0.25]]],
        'signals': [1, 10, 19],
        'min_max': [0, 64],
    },
    23: {
        'id': 23,
        'type': 3,
        'matrix': [[[10], [46, 64]], [[0.25], [0.75]]],
        'signals': [46, 55, 64],
        'min_max': [0, 64],
    },
    24: {
        'id': 24,
        'type': 4,
        'matrix': [[[10], [55]], [[], [0.1, 0.4]]],
        'signals': [0.1, 0.25, 0.4],
        'min_max': [0, 64],
    },
    25: {
        'id': 25,
        'type': 4,
        'matrix': [[[10], [55]], [[], [0.6, 0.9]]],
        'signals': [0.6, 0.75, 0.9],
        'min_max': [0, 64],
    },
    32: {
        'id': 32,
        'type': 2,
        'matrix': [[[7, 13], [55]], [[0.75], [0.25]]],
        'signals': [7, 10, 13],
        'min_max': [0, 58],
    },
    33: {
        'id': 33,
        'type': 3,
        'matrix': [[[10], [52, 58]], [[0.25], [0.75]]],
        'signals': [52, 55, 58],
        'min_max': [0, 58],
    },
    34: {
        'id': 34,
        'type': 4,
        'matrix': [[[10], [55]], [[], [0.2, 0.3]]],
        'signals': [0.2, 0.25, 0.3],
        'min_max': [0, 58],
    },
    35: {
        'id': 35,
        'type': 4,
        'matrix': [[[10], [55]], [[], [0.7, 0.8]]],
        'signals': [0.7, 0.75, 0.8],
        'min_max': [0, 58],
    },
}

QUESTIONS = {
    1: {
        'id': 1,
        'type': 1,
        'matrix': [[100, 0], [10, 10]],
        'total': 20,
        'min': 0,
        'max': 100
    },
    2: {
        'id': 2,
        'type': 2,
        'matrix': [[100, 0], []],
        'total': 20,
        'min': 0,
        'max': 100
    },
    3: {
        'id': 3,
        'type': 3,
        # Type 3 will have an fixed number specified for red, but it will not be displayed to the subjects
        'matrix': [[100, 0], [11, -1]],
        'total': 20,
        'min': 0,
        'max': 100
    },
    4: {
        'id': 4,
        'type': 1,
        'matrix': [[150, 0], [15, 15]],
        'total': 30,
        'min': 0,
        'max': 150
    },
    5: {
        'id': 5,
        'type': 2,
        'matrix': [[150, 0], []],
        'total': 30,
        'min': 0,
        'max': 150
    },
    6: {
        'id': 6,
        'type': 3,
        'matrix': [[150, 0], [23, -1]],
        'total': 30,
        'min': 0,
        'max': 150
    },
}
