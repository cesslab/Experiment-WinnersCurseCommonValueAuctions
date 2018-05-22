from typing import List, Dict
import random


class Question:
    LOW = 0
    HIGH = 1
    MIN = 0
    MAX = 1
    VALUE = 0
    PROBABILITY = 1

    def __init__(self, aid: int, atype: int, matrix: List = [], signals: List = [], min_max: List = []):
        self.aid = aid
        self.atype = atype
        self.matrix = matrix
        self.signals = signals
        self.signal_is_percentage = (atype == 4 or atype == 5)
        self.min_max = min_max
        self.cutoff = None

    @property
    def low_values(self):
        return self.matrix[Question.VALUE][Question.LOW]

    @property
    def high_values(self):
        return self.matrix[Question.VALUE][Question.HIGH]

    @property
    def low_probabilities(self):
        return self.matrix[Question.PROBABILITY][Question.LOW]

    @property
    def high_probabilities(self):
        return self.matrix[Question.PROBABILITY][Question.HIGH]

    @property
    def min_value(self):
        return self.min_max[Question.MIN]

    @property
    def max_value(self):
        return self.min_max[Question.MAX]

    def random_signal(self):
        return random.choice(self.signals)

    def range_low(self):
        assert (2 <= self.atype <= 5)
        if self.atype == 2:
            return self.low_values[Question.LOW]
        elif self.atype == 3:
            return self.high_values[Question.LOW]
        elif self.atype == 4:
            return self.high_probabilities[Question.LOW]
        else:
            return self.low_probabilities[Question.LOW]

    def range_high(self):
        assert (2 <= self.atype <= 5)
        if self.atype == 2:
            return self.low_values[Question.HIGH]
        elif self.atype == 3:
            return self.high_values[Question.HIGH]
        elif self.atype == 4:
            return self.high_probabilities[Question.HIGH]
        else:
            return self.low_probabilities[Question.HIGH]

    def low_update(self, signal):
        return (self.range_low() + signal) / 2

    def high_update(self, signal):
        return (self.range_high() + signal) / 2

    def low_value(self, player_signal, other_signal):
        if self.atype == 2:
            return (player_signal + other_signal) / 2
        else:
            return self.low_values[0]

    def high_value(self, player_signal, other_signal):
        if self.atype == 3:
            return (player_signal + other_signal) / 2
        else:
            return self.high_values[0]

    def low_probability(self, player_signal, other_signal):
        if self.atype == 5:
            return (player_signal + other_signal) / 2
        elif self.atype == 4:
            return 1 - (player_signal + other_signal) / 2
        else:
            return self.low_probabilities[0]

    def high_probability(self, player_signal, other_signal):
        if self.atype == 4:
            return (player_signal + other_signal) / 2
        elif self.atype == 5:
            return 1 - (player_signal + other_signal) / 2
        else:
            return self.high_probabilities[0]

    def __str__(self):
        return 'Question ' % self.aid

    def __rpr__(self):
        return "Question: {}, Type: {}".format(self.aid, self.atype)


class QuestionFactory:

    @staticmethod
    def questions(question_params: Dict) -> Dict[int, Question]:
        questions = {}
        for aid, params in question_params.items():
            questions[aid] = Question(
                aid=params['id'],
                atype=params['type'],
                matrix=params['matrix'],
                signals=params['signals'],
                min_max=params['min_max'],
            )
        return questions
