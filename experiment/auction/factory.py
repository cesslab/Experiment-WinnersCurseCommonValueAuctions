import random

from .auctions import (
    PhaseOneAuctionCollection, PhaseTwoAuctionCollection,
    PhaseThreeAuctionCollection, Auction)

from .treatment_one import (
    AUCTIONS, PHASE_ONE_AUCTION_PAIRS)


class AuctionCollectionFactory:
    @staticmethod
    def phase_one_rounds():
        return len(PHASE_ONE_AUCTION_PAIRS)

    @staticmethod
    def phase_two_rounds():
        return len(AUCTIONS)

    @staticmethod
    def phase_three_rounds():
        rounds = 0
        for auction in AUCTIONS:
            rounds += len(auction.signals)

        return rounds

    @staticmethod
    def phase_one_auctions():
        shuffled_pair = PHASE_ONE_AUCTION_PAIRS[:]
        random.shuffle(shuffled_pair)

        left_auctions = []
        right_auctions = []
        for pair_ids in shuffled_pair:
            random.shuffle(pair_ids)

            left_auction = AUCTIONS[pair_ids[0]]
            left_auctions.append(Auction(
                aid=left_auction['id'],
                atype=left_auction['type'],
                matrix=left_auction['matrix'],
                signals=left_auction['signals'],
                min_max=left_auction['min_max'],
            ))

            right_auction = AUCTIONS[pair_ids[1]]
            right_auctions.append(Auction(
                aid=right_auction['id'],
                atype=right_auction['type'],
                matrix=right_auction['matrix'],
                signals=right_auction['signals'],
                min_max=right_auction['min_max'],
            ))

        return PhaseOneAuctionCollection(left_auctions, right_auctions)

    @staticmethod
    def phase_two_auctions():
        auction_ids = [aid for aid, value in AUCTIONS]
        random.shuffle(auction_ids)
        auctions = []
        for aid in auction_ids:
            auction = AUCTIONS[aid]
            auctions.append(Auction(
                aid=auction['id'],
                atype=auction['type'],
                matrix=auction['matrix'],
                signals=auction['signals'],
                min_max=auction['min_max'],
            ))

        return PhaseTwoAuctionCollection(auctions)

    @staticmethod
    def phase_three_auctions():
        auctions = []
        signals = []
        for auction in AUCTIONS:
            for signal in auction.signals:
                auctions.append(auction)
                signals.append(signal)
        return PhaseThreeAuctionCollection(auctions, signals)
