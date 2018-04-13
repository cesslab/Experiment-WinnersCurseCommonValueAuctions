import random

from .auctions import (
    PhaseOneAuctionCollection, PhaseTwoAuctionCollection, PhaseThreeAuctionCollection)

from .treatment_one import AUCTIONS, PHASE_ONE_AUCTION_PAIRS, PHASE_TWO_AUCTION_GROUP


class AuctionCollectionFactory:
    @staticmethod
    def phase_one_rounds():
        return len(PHASE_ONE_AUCTION_PAIRS)

    @staticmethod
    def phase_two_rounds():
        rounds = 0
        for key, value in PHASE_TWO_AUCTION_GROUP.items():
            if key == 'auction_ids':
                rounds += len(value)
        return rounds

    @staticmethod
    def phase_three_rounds():
        rounds = 0
        for auction in AUCTIONS:
            rounds += len(auction.signals)

        return rounds

    @classmethod
    def phase_one_auctions(cls):
        shuffled_pair = random.shuffle(AUCTIONS)

        left_auctions = []
        right_auctions = []
        for pair in cls.PAIRS:
            left_auctions.append(AUCTIONS[pair[cls.LEFT_AUCTION]])
            right_auctions.append(AUCTIONS[pair[cls.RIGHT_AUCTION]])

        return PhaseOneAuctionCollection(left_auctions, right_auctions)

    @classmethod
    def phase_two_auctions(cls):
        auctions = []
        min_max_values = []
        for group in AuctionCollectionFactory.MIN_MAX:
            for auction_id in group['auction_ids']:
                auctions.append(AUCTIONS[auction_id])
                min_max_values.append(group['min_max'])

        return PhaseTwoAuctionCollection(auctions, min_max_values)

    @staticmethod
    def phase_three_auctions():
        auctions = []
        signals = []
        for auction in AUCTIONS:
            for signal in auction.signals:
                auctions.append(auction)
                signals.append(signal)
        return PhaseThreeAuctionCollection(auctions, signals)
