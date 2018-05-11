from exp.auction.factory import AuctionCollectionFactory


def test_auction_collection_contain_auctions():
    auctions = AuctionCollectionFactory.auctions()
    for aid, auction in auctions.items():
        for signal, bid in auction.bids.items():
            assert signal in auction.signals
