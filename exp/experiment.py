from exp.auction.factory import AuctionFactory as Factory
from exp.phases import (PhaseOne, PhaseTwo, PhaseThree)
from exp.treatment_one import (AUCTIONS, PHASE_ONE_AUCTION_PAIRS)


class Experiment:
    def __init__(self):
        self.auctions = Factory.auctions()
        self.phase_one = PhaseOne(self.auctions)
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
