from ._builtin import Page, WaitPage


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        # Instead of performing all of the querying here it is better to spread out acquisition of the
        # payoff auctions, bids, and cutoffs  in their respective rounds
        #
        # ----------------------------------------------------------------------------------------------
        # players = self.group.get_players()[:]
        # for i in range(len(players)):
        #     for player in players:
        #         # find a pair member
        #         pair_member = random.choice(players[:i] + players[i + 1:])
        #         # Choose a random round for phase one
        #         num_phase_one_rounds = PhaseOneConstants.num_rounds
        #         round_a = random.randint(1, num_phase_one_rounds)
        #         round_b = random.randint(1, num_phase_one_rounds)
        #         # retrieve the player's selected preference for round a ad b
        #         phase_one_auction_collection = player.participant.vars['phase_one_auctions']
        #
        #         preference_round_a = player.in_round(round_a).preference
        #         if preference_round_a == PhaseOneConstants.INDIFFERENT:
        #             if random.random() > 0.5:
        #                 auction = phase_one_auction_collection.left_auction(round_a)
        #             else:
        #                 auction = phase_one_auction_collection.right_auction(round_a)
        #         else:
        #             auction = phase_one_auction_collection.auctions[preference_round_a]

        # preference_round_b = player.in_round(round_b).preference
        pass


class Results(Page):
    pass


page_sequence = [
    ResultsWaitPage,
    Results
]
