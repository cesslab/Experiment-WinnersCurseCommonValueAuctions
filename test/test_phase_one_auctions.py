from auction.auctions import PhaseOneAuctionCollection, Auction
from auction.factory import AuctionCollectionFactory


def test_auction_collection_contain_auctions():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auction_collection()
    assert type(phase_one_auctions) is PhaseOneAuctionCollection


def test_left_auction_types():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auction_collection()
    for left_auction in phase_one_auctions.left_auctions:
        assert type(left_auction) is Auction


def test_right_auction_types():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auction_collection()
    for right_auction in phase_one_auctions.right_auctions:
        assert type(right_auction) is Auction


def test_rounds_equal_num_auction_pairs():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auction_collection()
    assert AuctionCollectionFactory.phase_one_rounds() == len(phase_one_auctions.left_auctions)
    assert AuctionCollectionFactory.phase_one_rounds() == len(phase_one_auctions.right_auctions)


def test_left_auctions_not_empty():
    assert AuctionCollectionFactory.phase_one_auction_collection().left_auctions


def test_right_auctions_not_empty():
    assert AuctionCollectionFactory.phase_one_auction_collection().right_auctions


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
    phase_one_auction = AuctionCollectionFactory.phase_one_auction_collection()
    for auction in phase_one_auction.left_auctions:
        assert auction.atype in [1, 2, 3, 4, 5]


def test_right_auctions_have_valid_type_ids():
    phase_one_auction = AuctionCollectionFactory.phase_one_auction_collection()
    for auction in phase_one_auction.right_auctions:
        assert auction.atype in [1, 2, 3, 4, 5]


def test_left_auction_values():
    phase_one_auction = AuctionCollectionFactory.phase_one_auction_collection()
    for auction in phase_one_auction.left_auctions:
        is_correct_auction_format(auction)


def test_right_auction_values():
    phase_one_auction = AuctionCollectionFactory.phase_one_auction_collection()
    for auction in phase_one_auction.right_auctions:
        is_correct_auction_format(auction)
