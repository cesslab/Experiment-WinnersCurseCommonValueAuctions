import random
from typing import Dict, List

from exp.auctions import Auction


class PhaseOne:
    def __init__(self, auctions: Dict[int, Auction], auction_pairs: List[List[int]]):
        self.left_auctions = []
        self.right_auctions = []
        self.preference = {}
        self.LEFT = 0
        self.RIGHT = 1
        self.INDIFFERENT = 2

        shuffled_pair = auction_pairs[:]
        random.shuffle(shuffled_pair)

        for pair_ids in shuffled_pair:
            random.shuffle(pair_ids)

            self.left_auctions.append(auctions[pair_ids[self.LEFT]])
            self.right_auctions.append(auctions[pair_ids[self.RIGHT]])

    def is_valid_auction_id(self, round_number: int, auction_id: int) -> bool:
        left_auction = self.left_auction(round_number)
        right_auction = self.right_auction(round_number)
        return auction_id in [left_auction.aid, right_auction.aid, -1]

    def get_auction_pair_dict(self, round_number: int) -> Dict[str, Auction]:
        return {
            'left_auction': self.left_auction(round_number),
            'right_auction': self.right_auction(round_number)
        }

    def left_auction(self, session_round: int) -> Auction:
        return self.left_auctions[session_round - 1]

    def right_auction(self, session_round: int) -> Auction:
        return self.right_auctions[session_round - 1]

    def get_preference(self, round_number) -> int:
        return self.preference[round_number]

    def set_preference(self, round_number: int, auction_id: int) -> None:
        self.preference[round_number] = auction_id

    def preferred_position(self, round_number) -> int:
        aid = self.get_preference(round_number)
        if aid == self.left_auction(round_number).aid:
            return self.LEFT
        elif aid == self.right_auction(round_number).aid:
            return self.RIGHT
        else:
            return self.INDIFFERENT

    def preferred_auction(self, round_number) -> Auction:
        aid = self.get_preference(round_number)
        if aid == self.left_auction(round_number).aid:
            return self.left_auction(round_number)
        else:
            return self.right_auction(round_number)

    def random_round(self) -> int:
        return random.randint(1, len(self.left_auctions))


class PhaseTwo:
    def __init__(self, auctions: Dict[int, Auction]):
        auction_ids = [aid for aid, value in auctions.items()]
        random.shuffle(auction_ids)
        shuffled_auctions = []
        for aid in auction_ids:
            shuffled_auctions.append(auctions[aid])
        self.auctions = shuffled_auctions

    def get_auction(self, session_round: int) -> Auction:
        return self.auctions[session_round - 1]

    def set_cutoff(self, round_number: int, cutoff: float) -> None:
        self.auctions[round_number - 1].cutoff = cutoff

    def random_round(self) -> int:
        return random.randint(1, len(self.auctions))


class PhaseThree:
    def __init__(self, auctions: Dict[int, Auction]):
        auction_signal_pairs = []
        keys = list(auctions.keys())
        random.shuffle(keys)
        for aid in keys:
            for signal in auctions[aid].signals:
                auction_signal_pairs.append(
                    {
                        'auction': auctions[aid],
                        'signal': signal
                    })
        self.auction_signal_pairs = auction_signal_pairs

    def auction(self, round_number: int) -> Auction:
        return self.auction_signal_pairs[round_number - 1]['auction']

    def signal(self, round_number: int):
        return self.auction_signal_pairs[round_number - 1]['signal']

    def low_update(self, round_number: int):
        signal = self.signal(round_number)
        return self.auction_signal_pairs[round_number - 1]['auction'].low_update(signal)

    def high_update(self, round_number: int):
        signal = self.signal(round_number)
        return self.auction_signal_pairs[round_number - 1]['auction'].high_update(signal)

    def set_bid(self, round_number: int, bid):
        self.auction(round_number).bids[self.signal(round_number)] = bid
