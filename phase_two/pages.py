from ._builtin import Page
from .models import Constants

from core.util import Participant


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.INSTRUCTIONS_ROUND


class CutoffSelectionPage(Page):
    form_model = 'player'
    form_fields = ['cutoff', 'clicked']

    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        return {'auction': experiment.phase_two.get_auction(self.round_number)}

    def cutoff_max(self):
        experiment = Participant.get_experiment(self.player)
        return experiment.phase_two.get_auction(self.round_number).max_value

    def cutoff_min(self):
        experiment = Participant.get_experiment(self.player)
        return experiment.phase_two.get_auction(self.round_number).min_value

    def error_message(self, values):
        if not int(values['clicked']) == 1:
            return ' You must specify how much would you be willing to receive to NOT participate in this lottery'

    def before_next_page(self):
        experiment = Participant.get_experiment(self.player)
        experiment.phase_two.set_cutoff(self.round_number, float(self.player.cutoff))

        self.player.auction = experiment.phase_two.get_auction(self.round_number).aid


page_sequence = [
    InstructionsPage, CutoffSelectionPage
]
