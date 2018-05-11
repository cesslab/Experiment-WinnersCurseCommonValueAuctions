from exp.auction.factory import AuctionFactory


def test_auction_collection_contain_auctions():
    auctions = AuctionFactory.auctions()
    for aid, auction in auctions.items():
        for signal, bid in auction.bids.items():
            assert signal in auction.signals
