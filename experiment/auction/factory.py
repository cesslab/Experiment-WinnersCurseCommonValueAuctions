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
                id=left_auction['id'],
                type=left_auction['type'],
                matrix=left_auction['matrix'],
                signals=left_auction['matrix'],
            ))

            right_auction = AUCTIONS[pair_ids[1]]
            right_auctions.append(Auction(
                id=right_auction['id'],
                type=right_auction['type'],
                matrix=right_auction['matrix'],
                signals=right_auction['matrix'],
            ))

        return PhaseOneAuctionCollection(left_auctions, right_auctions)

    @staticmethod
    def phase_two_auctions():
        auctions = []
        min_max_values = []
        # for group in PHASE_TWO_AUCTION_GROUP:
        #     for auction_id in group['auction_ids']:
        #         auctions.append(AUCTIONS[auction_id])
        #         min_max_values.append(group['min_max'])
        #
        # return PhaseTwoAuctionCollection(auctions, min_max_values)

    @staticmethod
    def phase_three_auctions():
        auctions = []
        signals = []
        for auction in AUCTIONS:
            for signal in auction.signals:
                auctions.append(auction)
                signals.append(signal)
        return PhaseThreeAuctionCollection(auctions, signals)
