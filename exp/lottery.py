from typing import List, Dict


class Lottery:
    RED = 0
    BLUE = 1
    VALUE = 0
    NUMBER = 1

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
    def red_value(self):
        return self.matrix[Lottery.VALUE][Lottery.RED]

    @property
    def blue_value(self):
        return self.matrix[Lottery.VALUE][Lottery.BLUE]

    @property
    def red_number(self):
        assert self.ltype == 1
        return self.matrix[Lottery.NUMBER][Lottery.RED]

    @property
    def blue_number(self):
        assert self.ltype == 1
        return self.matrix[Lottery.NUMBER][Lottery.BLUE]

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
