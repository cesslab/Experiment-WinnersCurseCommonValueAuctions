from core.experiment import Experiment
from core.payment import MethodThreeResults, MethodOneResults, MethodTwoResults


class Participant:
    @staticmethod
    def get_experiment(player) -> Experiment:
        return player.participant.vars['experiment']

    @staticmethod
    def set_experiment(player, experiment: Experiment) -> None:
        player.participant.vars['experiment'] = experiment

    @staticmethod
    def set_payment_one_results(player, payment_results: MethodOneResults) -> None:
        player.participant.vars['payment_one_results'] = payment_results

    @staticmethod
    def get_payment_one_results(player) -> MethodOneResults:
        return player.participant.vars['payment_one_results']

    @staticmethod
    def set_payment_two_results(player, payment_results: MethodTwoResults) -> None:
        player.participant.vars['payment_two_results'] = payment_results

    @staticmethod
    def set_payment_three_results(player, payment_results: MethodThreeResults) -> None:
        player.participant.vars['payment_three_results'] = payment_results

    @staticmethod
    def get_payment_two_results(player) -> MethodTwoResults:
        return player.participant.vars['payment_two_results']

    @staticmethod
    def get_payment_three_results(player) -> MethodThreeResults:
        return player.participant.vars['payment_three_results']
