from exp.experiment import Experiment
from exp.auctions import Auction


def test_left_auction_types():
    experiment = Experiment()
    for left_auction in experiment.phase_one.left_auctions:
        assert type(left_auction) is Auction


def test_right_auction_types():
    experiment = Experiment()
    for right_auction in experiment.phase_one.right_auctions:
        assert type(right_auction) is Auction


def test_rounds_equal_num_auction_pairs():
    experiment = Experiment()
    assert experiment.phase_one_rounds() == len(experiment.phase_one.left_auctions)
    assert experiment.phase_one_rounds() == len(experiment.phase_one.right_auctions)


def test_left_auctions_not_empty():
    experiment = Experiment()
    assert experiment.phase_one.left_auctions


def test_right_auctions_not_empty():
    experiment = Experiment()
    assert experiment.phase_one.right_auctions


def is_correct_auction_format(auction):
    aid = auction.aid
    atype = auction.atype
    temp = "Auction {} type {} must have {{}} value(s) in the {{}} position"
    message = temp.format(aid, atype)
    if atype == 1:
        assert len(auction.low_values) == 1, message.format(1, 'low_values')
        assert len(auction.high_values) == 1, message.format(1, 'high_values')
        assert len(auction.low_probabilities) == 1, message.format(1, 'low_probabilities')
        assert len(auction.high_probabilities) == 1, message.format(1, 'high_probabilities')
    elif atype == 2:
        assert len(auction.low_values) == 2, message.format(2, 'low_values')
        assert len(auction.high_values) == 1, message.format(1, 'high_values')
        assert len(auction.low_probabilities) == 1, message.format(1, 'low_probabilities')
        assert len(auction.high_probabilities) == 1, message.format(1, 'high_probabilities')
    elif atype == 3:
        assert len(auction.low_values) == 1, message.format(1, 'low_values')
        assert len(auction.high_values) == 2, message.format(2, 'high_values')
        assert len(auction.low_probabilities) == 1, message.format(1, 'low_probabilities')
        assert len(auction.high_probabilities) == 1, message.format(1, 'high_probabilities')
    elif atype == 4:
        assert len(auction.low_values) == 1, message.format(1, 'low_values')
        assert len(auction.high_values) == 1, message.format(1, 'high_values')
        assert len(auction.low_probabilities) == 0, message.format(0, 'low_probabilities')
        assert len(auction.high_probabilities) == 2, message.format(2, 'high_probabilities')
    elif atype == 5:
        assert len(auction.low_values) == 1, message.format(1, 'low_values')
        assert len(auction.high_values) == 1, message.format(1, 'high_values')
        assert len(auction.low_probabilities) == 2, message.format(2, 'low_probabilities')
        assert len(auction.high_probabilities) == 0, message.format(0, 'high_probabilities')


def test_left_auctions_have_valid_type_ids():
    experiment = Experiment()
    for auction in experiment.phase_one.left_auctions:
        assert auction.atype in [1, 2, 3, 4, 5]


def test_right_auctions_have_valid_type_ids():
    experiment = Experiment()
    for auction in experiment.phase_one.right_auctions:
        assert auction.atype in [1, 2, 3, 4, 5]


def test_left_auction_values():
    experiment = Experiment()
    for auction in experiment.phase_one.left_auctions:
        is_correct_auction_format(auction)


def test_right_auction_values():
    experiment = Experiment()
    for auction in experiment.phase_one.right_auctions:
        is_correct_auction_format(auction)
