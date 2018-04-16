from auction.factory import AuctionCollectionFactory
from auction.auctions import PhaseOneAuctionCollection, Auction


def test_auction_collection_contain_auctions():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auctions()
    assert type(phase_one_auctions) is PhaseOneAuctionCollection


def test_left_auction_types():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auctions()
    for left_auction in phase_one_auctions.left_auctions:
        assert type(left_auction) is Auction


def test_right_auction_types():
    phase_one_auctions = AuctionCollectionFactory.phase_one_auctions()
    for right_auction in phase_one_auctions.right_auctions:
        assert type(right_auction) is Auction


def test_rounds_not_zero():
    assert AuctionCollectionFactory.phase_one_rounds() > 0


def test_left_auctions_not_empty():
    assert AuctionCollectionFactory.phase_one_auctions().left_auctions


def test_right_auctions_not_empty():
    assert AuctionCollectionFactory.phase_one_auctions().right_auctions


def is_correct_auction_format(auction):
    aid = auction .aid
    atype = auction.atype
    temp = "Auction {} type {} must have {{}} value(s) in the {{}} position"
    message = temp.format(aid, atype)
    if atype == 1:
        assert len(auction.val_low) == 1, message.format(1, 'val_low')
        assert len(auction.val_high) == 1, message.format(1, 'val_high')
        assert len(auction.prob_low) == 1, message.format(1, 'prob_low')
        assert len(auction.prob_high) == 1, message.format(1, 'prob_high')
    elif atype == 2:
        assert len(auction.val_low) == 2, message.format(2, 'val_low')
        assert len(auction.val_high) == 1, message.format(1, 'val_high')
        assert len(auction.prob_low) == 1, message.format(1, 'prob_low')
        assert len(auction.prob_high) == 1, message.format(1, 'prob_high')
    elif atype == 3:
        assert len(auction.val_low) == 1, message.format(1, 'val_low')
        assert len(auction.val_high) == 2, message.format(2, 'val_high')
        assert len(auction.prob_low) == 1, message.format(1, 'prob_low')
        assert len(auction.prob_high) == 1, message.format(1, 'prob_high')
    elif atype == 4:
        assert len(auction.val_low) == 1, message.format(1, 'val_low')
        assert len(auction.val_high) == 1, message.format(1, 'val_high')
        assert len(auction.prob_low) == 0, message.format(0, 'prob_low')
        assert len(auction.prob_high) == 2, message.format(2, 'prob_high')
    elif atype == 5:
        assert len(auction.val_low) == 1, message.format(1, 'val_low')
        assert len(auction.val_high) == 1, message.format(1, 'val_high')
        assert len(auction.prob_low) == 2, message.format(2, 'prob_low')
        assert len(auction.prob_high) == 0, message.format(0, 'prob_high')


def test_left_auctions_have_valid_type_ids():
    phase_one_auction = AuctionCollectionFactory.phase_one_auctions()
    for auction in phase_one_auction.left_auctions:
        assert auction.atype in [1, 2, 3, 4, 5]


def test_right_auctions_have_valid_type_ids():
    phase_one_auction = AuctionCollectionFactory.phase_one_auctions()
    for auction in phase_one_auction.right_auctions:
        assert auction.atype in [1, 2, 3, 4, 5]


def test_left_auction_values():
    phase_one_auction = AuctionCollectionFactory.phase_one_auctions()
    for auction in phase_one_auction.left_auctions:
        is_correct_auction_format(auction)


def test_right_auction_values():
    phase_one_auction = AuctionCollectionFactory.phase_one_auctions()
    for auction in phase_one_auction.right_auctions:
        is_correct_auction_format(auction)
