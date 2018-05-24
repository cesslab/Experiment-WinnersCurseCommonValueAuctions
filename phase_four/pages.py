from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage

from exp.util import Participant


class InstructionsPage(Page):
    def is_displayed(self):
        return self.round_number == 1


class RollDicePage(Page):
    def is_displayed(self):
        return self.round_number == 1

    def error_message(self, values):
        if not ('side' not in values or 1 <= int(values['side']) <= 6):
            return 'You must roll the die before continuing.'

    def before_next_page(self):
        experiment = Participant.get_experiment(self.player)
        experiment.phase_four.set_die_side(self.player.die_side)


class MinBuyoutBetForLotteryPage(Page):
    form_model = 'player'
    form_fields = ['cutoff', 'clicked']

    def vars_for_template(self):
        experiment = Participant.get_experiment(self.player)
        return {'auction': experiment.phase_four.get_lottery(self.round_number)}

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

        experiment.phase_two.set_cutoff(self.round_number, self.player.cutoff)
        self.player.question = experiment.phase_two.get_auction(self.round_number).aid


# class ResultsWaitPage(WaitPage):
#
#     def after_all_players_arrive(self):
#         pass


page_sequence = [
    InstructionsPage,
    RollDicePage,
    MinBuyoutBetForLotteryPage,
    # ResultsWaitPage,
]
