from auction.auctions import PhaseThreeAuctionCollection, Auction
from auction.factory import AuctionCollectionFactory


def test_auction_collection_not_empty():
    assert AuctionCollectionFactory.phase_three_auction_collection()


def test_auction_collection_contain_auctions():
    auction_collection = AuctionCollectionFactory.phase_three_auction_collection()
    assert type(auction_collection) is PhaseThreeAuctionCollection


def test_rounds_not_zero():
    assert AuctionCollectionFactory.phase_three_rounds() > 0


def test_rounds_equals_signals_times_auctions():
    rounds = AuctionCollectionFactory.phase_three_rounds()
    auction_collection = AuctionCollectionFactory.phase_three_auction_collection()
    assert rounds == len(auction_collection.auction_signal_pairs)


def test_factory_auction_types():
    auction_collection = AuctionCollectionFactory.phase_three_auction_collection()
    rounds = AuctionCollectionFactory.phase_three_rounds()
    for game_round in range(1, rounds + 1):
        assert (type(auction_collection.auction(game_round)) is Auction)


def test_auction_signal_within_range():
    auction_signal_pair = AuctionCollectionFactory.phase_three_auction_collection().auction_signal_pairs
    for pair in auction_signal_pair:
        auction = pair['auction']
        signal = pair['signal']
        assert auction.range_low() <= signal <= auction.range_high(), "auction {}".format(auction.aid)

