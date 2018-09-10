from ._builtin import Page
from .models import Constants

from core.util import Participant


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class BidPage(Page):
    form_model = 'player'
    form_fields = ['bid']

    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        auction = experiment.phase_three.auction(self.round_number)

        if auction.signal_is_percentage:
            signals = ", ".join(["{}%".format(round(s * 100)) for s in auction.signals])
        else:
            signals = ", ".join(map(str, auction.signals))

        return {
            'signal_is_percentage': auction.signal_is_percentage,
            'auction': auction,
            'signal': experiment.phase_three.signal(self.round_number),
            'low_update': experiment.phase_three.low_update(self.round_number),
            'high_update': experiment.phase_three.high_update(self.round_number),
            'signals': signals,
        }

    def bid_error_message(self, bid):
        experiment = Participant.get_experiment(self.player)
        min_value = experiment.phase_three.auction(self.round_number).min_value
        max_value = experiment.phase_three.auction(self.round_number).max_value
        if not min_value <= bid <= max_value:
            return 'The bid value must be between {} and {}.'.format(min_value, max_value)

    def before_next_page(self):
        experiment = Participant.get_experiment(self.player)
        experiment.phase_three.set_bid(self.round_number, float(self.player.bid))

        self.player.auction = experiment.phase_three.auction(self.round_number).aid
        self.player.signal = experiment.phase_three.signal(self.round_number)
        self.player.low_update = experiment.phase_three.low_update(self.round_number)
        self.player.high_update = experiment.phase_three.high_update(self.round_number)


page_sequence = [
    InstructionsPage, BidPage,
]
