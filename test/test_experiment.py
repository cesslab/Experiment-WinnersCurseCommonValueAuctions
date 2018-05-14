from exp.experiment import Experiment
from exp.auctions import Auction


def test_experiment_generates_auctions():
    experiment = Experiment()
    assert experiment.auctions is not None
    assert len(experiment.auctions) > 0
    for aid, auction in experiment.auctions.items():
        assert type(auction) is Auction
        assert type(aid) is int



