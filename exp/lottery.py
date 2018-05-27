from typing import List, Dict


class Lottery:
    HIGH = 0
    LOW = 1
    VALUE = 0
    NUMBER = 1
    ALL_KNOWN = 1
    COMPOUND_RISK = 2
    AMBIGUITY = 3
    BET_HIGH_RED = 0
    BET_HIGH_BLUE = 1

    def __init__(self, lid: int, ltype: int, total: int, matrix: List, min_cutoff: int, max_cutoff: int):
        self.lid = lid
        self.ltype = ltype
        self.total = total
        self.matrix = matrix
        self.max_cutoff = max_cutoff
        self.min_cutoff = min_cutoff

        self.cutoff = None
        self.bet = None

    @property
    def high_value(self):
        return self.matrix[Lottery.VALUE][Lottery.HIGH]

    @property
    def low_value(self):
        return self.matrix[Lottery.VALUE][Lottery.LOW]

    @property
    def number_red(self):
        assert self.ltype == 1 or self.ltype == 3
        return self.matrix[Lottery.NUMBER][Lottery.HIGH]

    @property
    def number_blue(self):
        assert self.ltype == 1
        return self.matrix[Lottery.NUMBER][Lottery.LOW]

    def has_number_blue(self):
        return self.ltype == 1

    def has_number_red(self):
        return self.ltype == 1 or self.ltype == 3

    def __str__(self):
        return 'Lottery ' % self.lid

    def __rpr__(self):
        return "Lottery: {}, Type: {}".format(self.lid, self.ltype)


class LotteryFactory:

    @staticmethod
    def questions(lottery_params: Dict) -> Dict[int, Lottery]:
        lotteries = {}
        for lid, params in lottery_params.items():
            lotteries[lid] = Lottery(
                lid=params['id'],
                ltype=params['type'],
                total=params['total'],
                matrix=params['matrix'],
                min_cutoff=params['min'],
                max_cutoff=params['max'],
            )
        return lotteries
