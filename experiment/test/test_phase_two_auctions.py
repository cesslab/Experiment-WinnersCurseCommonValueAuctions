from auction.factory import AuctionCollectionFactory
from auction.auctions import PhaseTwoAuctionCollection, Auction


def test_auction_collection_not_empty():
    assert AuctionCollectionFactory.phase_two_auctions()


def test_auction_collection_contain_auctions():
    auction_collection = AuctionCollectionFactory.phase_two_auctions()
    assert type(auction_collection) is PhaseTwoAuctionCollection


def test_rounds_not_zero():
    assert AuctionCollectionFactory.phase_two_rounds() > 0


def test_auction_min_is_less_than_max():
    for auction in AuctionCollectionFactory.phase_two_auctions():
        assert auction.min_value <= auction.max_value
