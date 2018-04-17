from auction.auctions import PhaseTwoAuctionCollection
from auction.factory import AuctionCollectionFactory


def test_auction_collection_not_empty():
    assert AuctionCollectionFactory.phase_two_auctions()


def test_auction_collection_contain_auctions():
    auction_collection = AuctionCollectionFactory.phase_two_auctions()
    assert type(auction_collection) is PhaseTwoAuctionCollection


def test_rounds_number_is_equal_to_auctions():
    auction_collection = AuctionCollectionFactory.phase_two_auctions()
    assert AuctionCollectionFactory.phase_two_rounds() == len(auction_collection.auctions)


def test_auction_min_is_less_than_max():
    for auction in AuctionCollectionFactory.phase_two_auctions().auctions:
        assert auction.min_value <= auction.max_value
