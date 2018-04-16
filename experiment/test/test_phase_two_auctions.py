from auction.factory import AuctionCollectionFactory
from auction.auctions import PhaseOneAuctionCollection, Auction


def test_auction_collection_not_empty():
    assert AuctionCollectionFactory.phase_two_auctions()


def test_auction_collection_contain_auctions():
    auction_collection = AuctionCollectionFactory.phase_one_auctions()
    assert type(auction_collection) is PhaseOneAuctionCollection


def test_rounds_not_zero():
    assert AuctionCollectionFactory.phase_two_rounds() > 0
