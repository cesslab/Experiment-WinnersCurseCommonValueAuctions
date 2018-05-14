from exp.auctions import AuctionFactory
from exp.phases import (PhaseOne, PhaseTwo, PhaseThree)
from exp.parameters import (AUCTIONS, PHASE_ONE_AUCTION_PAIRS)


class Experiment:
    def __init__(self):
        self.auctions = AuctionFactory.auctions(AUCTIONS)
        self.phase_one = PhaseOne(self.auctions, PHASE_ONE_AUCTION_PAIRS)
        self.phase_two = PhaseTwo(self.auctions)
        self.phase_three = PhaseThree(self.auctions)

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


