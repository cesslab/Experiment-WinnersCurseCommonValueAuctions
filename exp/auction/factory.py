import random
from typing import Dict

from .auctions import (PhaseOneAuctionCollection, PhaseTwoAuctionCollection, PhaseThreeAuctionCollection, Auction)
from exp.treatment_one import (AUCTIONS, PHASE_ONE_AUCTION_PAIRS)


class AuctionCollectionFactory:
    @staticmethod
    def phase_one_rounds() -> int:
        return len(PHASE_ONE_AUCTION_PAIRS)

    @staticmethod
    def phase_two_rounds() -> int:
        return len(AUCTIONS)

    @staticmethod
    def phase_three_rounds() -> int:
        rounds = 0
        for aid, auction_params in AUCTIONS.items():
            rounds += len(auction_params['signals'])

        return rounds

    @staticmethod
    def auctions() -> Dict[int, Auction]:
        auctions = {}
        for aid, params in AUCTIONS.items():
            auctions[aid] = Auction(
                aid=params['id'],
                atype=params['type'],
                matrix=params['matrix'],
                signals=params['signals'],
                min_max=params['min_max'],
            )
        return auctions

    @staticmethod
    def phase_one_auction_collection(auctions) -> PhaseOneAuctionCollection:
        shuffled_pair = PHASE_ONE_AUCTION_PAIRS[:]
        random.shuffle(shuffled_pair)

        left_auctions = []
        right_auctions = []
        for pair_ids in shuffled_pair:
            random.shuffle(pair_ids)

            left_auctions.append(auctions[pair_ids[0]])
            right_auctions.append(auctions[pair_ids[1]])

        return PhaseOneAuctionCollection(left_auctions, right_auctions, auctions)

    @staticmethod
    def phase_two_auction_collection(auctions) -> PhaseTwoAuctionCollection:
        auction_ids = [aid for aid, value in auctions.items()]
        random.shuffle(auction_ids)
        shuffled_auctions = []
        for aid in auction_ids:
            shuffled_auctions.append(auctions[aid])

        return PhaseTwoAuctionCollection(shuffled_auctions)

    @staticmethod
    def phase_three_auction_collection(auctions) -> PhaseThreeAuctionCollection:
        auction_signal_pairs = []
        keys = list(auctions.keys())
        random.shuffle(keys)
        for aid in keys:
            for signal in auctions[aid]['signals']:
                auction_signal_pairs.append(
                    {
                        'auction': auctions[aid],
                        'signal': signal
                    })

        return PhaseThreeAuctionCollection(auction_signal_pairs)
