from exp.auctions import AuctionFactory
from exp.questions import QuestionFactory
from exp.phases import (PhaseOne, PhaseTwo, PhaseThree, PhaseFour)
from exp.parameters import (AUCTIONS, PHASE_ONE_AUCTION_PAIRS, QUESTIONS)


class Experiment:
    ENDOWMENT = 100
    CONVERSION_RATE = 0.5

    def __init__(self):
        self.auctions = AuctionFactory.auctions(AUCTIONS)
        self.questions = QuestionFactory.questions(QUESTIONS)
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
