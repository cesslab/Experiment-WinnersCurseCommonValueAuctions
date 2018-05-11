from exp.experiment import Experiment


class Participant:
    @staticmethod
    def get_experiment(player) -> Experiment:
        return player.participant.vars['PaymentMethodOne']

    @staticmethod
    def set_experiment(player, experiment: Experiment) -> None:
        player.participant.vars['experiment'] = experiment
