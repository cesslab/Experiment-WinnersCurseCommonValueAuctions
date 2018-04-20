import random

from ._builtin import Page, WaitPage


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        # Instead of performing all of the querying here it is better to spread out acquisition of the
        # payoff auctions, bids, and cutoffs  in their respective rounds
        #
        # ----------------------------------------------------------------------------------------------
        players = self.group.get_players()[:]
        for i in range(len(players)):
            for player in players:
                other_player = random.choice(players[:i] + players[i + 1:])
                if self.player_win_auction(player, other_player):
                    pass
                else:
                    player.payoff = 0

    def player_win_auction(self, player, other):
        player_participant_vars = player.participant.vars
        other_participant_vars = other.participant.vars
        aid = player_participant_vars['auction_a_id']
        player_auction = player_participant_vars['auctions'][aid]
        other_auction = other_participant_vars['auctions'][aid]

        # Get the player's bid for the first randomly chosen payoff relevant auction-signal pair
        player_bid = player_auction.bids[player_auction.random_signal]
        other_bid = other_auction.bids[player_auction.random_signal]

        if player_bid == other_bid:
            return random.randint(0, 1) == 1
        else:
            return player_bid > other_bid


class Results(Page):
    pass


page_sequence = [
    ResultsWaitPage,
    Results
]
