from exp.auction import PhaseTwoAuctionCollection
from exp.auction.factory import AuctionFactory


def test_auction_collection_not_empty():
    assert AuctionFactory.phase_two_auction_collection()


def test_auction_collection_contain_auctions():
    auction_collection = AuctionFactory.phase_two_auction_collection()
    assert type(auction_collection) is PhaseTwoAuctionCollection


def test_rounds_number_is_equal_to_auctions():
    auction_collection = AuctionFactory.phase_two_auction_collection()
    assert AuctionFactory.phase_two_rounds() == len(auction_collection.auctions)


def test_auction_min_is_less_than_max():
    for auction in AuctionFactory.phase_two_auction_collection().auctions:
        assert auction.min_value <= auction.max_value


def test_type_four_five_auctions_have_float_signals():
    for auction in AuctionFactory.phase_two_auction_collection().auctions:
        if auction.atype == 4 or auction.atype == 5:
            for signal in auction.signals:
                assert isinstance(signal, float)
        else:
            for signal in auction.signals:
                assert isinstance(signal, int)
