from core.experiment import Experiment


def test_auction_collection_pair_not_empty():
    experiment = Experiment()
    assert experiment.phase_three.auction_signal_pairs


def test_rounds_equals_signals_times_auctions():
    experiment = Experiment()
    rounds = experiment.phase_three_rounds()
    assert rounds == len(experiment.phase_three.auction_signal_pairs)


def test_auction_signal_within_range():
    experiment = Experiment()
    auction_signal_pair = experiment.phase_three.auction_signal_pairs
    for pair in auction_signal_pair:
        auction = pair['auction']
        signal = pair['signal']
        assert auction.range_low() <= signal <= auction.range_high(), "auction {}".format(auction.aid)

