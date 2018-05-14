from exp.experiment import Experiment
from exp.payment import Results


class Participant:
    @staticmethod
    def get_experiment(player) -> Experiment:
        return player.participant.vars['experiment']

    @staticmethod
    def set_experiment(player, experiment: Experiment) -> None:
        player.participant.vars['experiment'] = experiment

    @staticmethod
    def set_payment_one_results(player, payment_results: Results) -> None:
        player.participant.vars['payment_one_results'] = payment_results

    @staticmethod
    def get_payment_one_results(player) -> Results:
        return player.participant.vars['payment_one_results']

    @staticmethod
    def set_payment_two_results(player, payment_results: Results) -> None:
        player.participant.vars['payment_two_results'] = payment_results

    @staticmethod
    def get_payment_two_results(player) -> Results:
        return player.participant.vars['payment_two_results']
