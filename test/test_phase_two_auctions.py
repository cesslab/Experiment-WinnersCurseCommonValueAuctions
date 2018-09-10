from core.experiment import Experiment


def test_auction_not_empty():
    experiment = Experiment()
    assert experiment.phase_two.auctions


def test_auction_min_is_less_than_max():
    experiment = Experiment()
    for auction in experiment.phase_two.auctions:
        assert auction.min_value <= auction.max_value


def test_type_four_five_auctions_have_float_signals():
    experiment = Experiment()
    for auction in experiment.phase_two.auctions:
        if auction.atype == 4 or auction.atype == 5:
            for signal in auction.signals:
                assert isinstance(signal, float)
        else:
            for signal in auction.signals:
                assert isinstance(signal, int)
