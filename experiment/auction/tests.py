import unittest

from .treatment_1 import AuctionCollectionFactory
from .auctions import PhaseOneAuctionCollection, Auction


class TestPhaseOneAuctions(unittest.TestCase):
    def test_phase_one_auction_factory(self):
        phase_one_auctions = AuctionCollectionFactory.phase_one_auctions()
        self.assertTrue(type(phase_one_auctions) is PhaseOneAuctionCollection)

    def test_phase_one_left_auctions(self):
        phase_one_auctions = AuctionCollectionFactory.phase_one_auctions()
        for left_auction in phase_one_auctions.left_auctions:
            self.assertTrue(type(left_auction) is Auction)

    def test_phase_one_right_auctions(self):
        phase_one_auctions = AuctionCollectionFactory.phase_one_auctions()
        for left_auction in phase_one_auctions.left_auctions:
            self.assertTrue(type(left_auction) is Auction)

    def test_rounds_not_zero(self):
        self.assertTrue(AuctionCollectionFactory.phase_one_rounds())

    def test_auctions_not_zero(self):
        self.assertTrue(AuctionCollectionFactory.phase_one_auctions())

    def test_left_auctions(self):
        self.assertTrue(AuctionCollectionFactory.phase_one_auctions().left_auctions)

    def test_right_auctions(self):
        self.assertTrue(AuctionCollectionFactory.phase_one_auctions().right_auctions)

    def is_correct_auction_format(self, auction):
        if auction.type == 1:
            self.assertEqual(len(auction.val_low), 1,
                             msg="Auction id={} must have only 1 value in the val_low position".format(auction.id))
            self.assertEqual(len(auction.val_high), 1,
                             msg="Auction id={} must have only 1 value in the val_high position".format(auction.id))
            self.assertEqual(len(auction.prob_low), 1,
                             msg="Auction id={} must have only 1 value in the prob_low position".format(auction.id))
            self.assertEqual(len(auction.prob_high), 1,
                             msg="Auction id={} must have only 1 value in the prob_high position".format(auction.id))

        elif auction.type == 2:
            self.assertEqual(len(auction.val_low), 2,
                            msg="Auction id={} must have only 2 values in the val_low position".format(auction.id))
            self.assertEqual(len(auction.val_high), 1,
                            msg="Auction id={} must have only 1 value in the val_high position".format(auction.id))
            self.assertEqual(len(auction.prob_low), 1,
                            msg="Auction id={} must have only 1 value in the prob_low position".format(auction.id))
            self.assertEqual(len(auction.prob_high), 1,
                            msg="Auction id={} must have only 1 value in the prob_high position".format(auction.id))
        elif auction.type == 3:
            self.assertEqual(len(auction.val_low), 1,
                            msg="Auction id={} must have only 1 value in the val_low position".format(auction.id))
            self.assertEqual(len(auction.val_high), 2,
                            msg="Auction id={} must have only 2 values in the val_high position".format(auction.id))
            self.assertEqual(len(auction.prob_low), 1,
                            msg="Auction id={} must have only 1 value in the prob_low position".format(auction.id))
            self.assertEqual(len(auction.prob_high), 1,
                            msg="Auction id={} must have only 1 value in the prob_high position".format(auction.id))
        elif auction.type == 4:
            self.assertEqual(len(auction.val_low), 1,
                            msg="Auction id={} must have only 1 value in the val_low position".format(auction.id))
            self.assertEqual(len(auction.val_high), 1,
                            msg="Auction id={} must have only 1 value in the val_high position".format(auction.id))
            self.assertEqual(len(auction.prob_low), 2,
                            msg="Auction id={} must have only 2 values in the prob_low position".format(auction.id))
            self.assertEqual(len(auction.prob_high), 0,
                            msg="Auction id={} must have only NO values in the prob_high position".format(auction.id))
        elif auction.type == 5:
            self.assertEqual(len(auction.val_low), 1,
                            msg="Auction id={} must have only 1 value in the val_low position".format(auction.id))
            self.assertEqual(len(auction.val_high), 1,
                            msg="Auction id={} must have only 1 value in the val_high position".format(auction.id))
            self.assertEqual(len(auction.prob_low), 0,
                            msg="Auction id={} must have only no values in the prob_low position".format(auction.id))
            self.assertEqual(len(auction.prob_high), 2,
                            msg="Auction id={} must have only NO values in the prob_high position".format(auction.id))

    def test_left_auction_values(self):
        phase_one_auction = AuctionCollectionFactory.phase_one_auctions()
        for auction in phase_one_auction.left_auctions:
            self.assertTrue(auction.type in [1, 2, 3, 4, 5])
            self.is_correct_auction_format(auction)

    def test_right_auction_values(self):
        phase_one_auction = AuctionCollectionFactory.phase_one_auctions()
        for auction in phase_one_auction.right_auctions:
            self.assertTrue(auction.type in [1, 2, 3, 4, 5])
            self.is_correct_auction_format(auction)


if __name__ == '__main__':
    unittest.main()