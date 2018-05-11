from phase_one._builtin import Page
from .models import Constants

from exp.util import Participant


class SelectAuctionPage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        return experiment.phase_one.get_auction_pair_dict(self.round_number)

    def preference_error_message(self, value):
        experiment = Participant.get_experiment(self.player)
        if not experiment.phase_one.is_valid_auction_id(self.round_number, int(value)):
            return 'You must choose Auction A, Auction B, or Indifferent'

    def before_next_page(self):
        experiment = Participant.get_experiment(self.player)

        self.player.left_auction = experiment.phase_one.left_auction(self.round_number)
        self.player.right_auction = experiment.phase_one.right_auction(self.round_number)

        experiment.phase_one.set_preference(self.round_number, self.player.preference)


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class Results(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False


page_sequence = [
    InstructionsPage,
    SelectAuctionPage,
]
