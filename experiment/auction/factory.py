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
        for aid, auction_params in AUCTIONS.items():
            rounds += len(auction_params['signals'])

        return rounds

    @staticmethod
    def phase_one_auctions():
        auctions = {}
        for aid, params in AUCTIONS.items():
            auctions[aid] = Auction(
                aid=params['id'],
                atype=params['type'],
                matrix=params['matrix'],
                signals=params['signals'],
                min_max=params['min_max'],
            )

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

        return PhaseOneAuctionCollection(left_auctions, right_auctions, auctions)

    @staticmethod
    def phase_two_auctions():
        auction_ids = [aid for aid, value in AUCTIONS.items()]
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
        auction_signal_pairs = []
        for aid, auction_params in AUCTIONS.items():
            for signal in auction_params['signals']:
                auction_signal_pairs.append(
                    {
                        'auction': Auction(
                            aid=auction_params['id'],
                            atype=auction_params['type'],
                            matrix=auction_params['matrix'],
                            signals=auction_params['signals'],
                            min_max=auction_params['min_max']),
                        'signal': signal
                    })

        random.shuffle(auction_signal_pairs)
        return PhaseThreeAuctionCollection(auction_signal_pairs)
