from core.auctions import AuctionFactory
from core.lottery import LotteryFactory
from core.phases import (PhaseOne, PhaseTwo, PhaseThree, PhaseFour)
from core.parameters import (AUCTIONS, PHASE_ONE_AUCTION_PAIRS, QUESTIONS)


class Experiment:
    ENDOWMENT = 10
    CONVERSION_RATE = 0.125
    SHOW_UP_FEE = 10
    PART_ONE_WEIGHT = 0.75
    PART_TWO_WEIGHT = 0.25

    def __init__(self):
        self.auctions = AuctionFactory.auctions(AUCTIONS)
        self.questions = LotteryFactory.questions(QUESTIONS)
        self.phase_one = PhaseOne(self.auctions, PHASE_ONE_AUCTION_PAIRS)
        self.phase_two = PhaseTwo(self.auctions)
        self.phase_three = PhaseThree(self.auctions)
        self.phase_four = PhaseFour(self.questions)

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
    def phase_four_rounds() -> int:
        rounds = 6
        return rounds
