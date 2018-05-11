from typing import Dict

from exp.auctions import Auction
from exp.treatment_one import AUCTIONS


class AuctionFactory:

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

