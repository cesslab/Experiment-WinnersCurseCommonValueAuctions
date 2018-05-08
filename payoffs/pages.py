import random

from auction.factory import AuctionCollectionFactory

from ._builtin import Page, WaitPage

from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        # Instead of performing all of the querying here it is better to spread out acquisition of the
        # payoff auctions, bids, and cutoffs  in their respective rounds
        #
        # ----------------------------------------------------------------------------------------------
        players = self.group.get_players()[:]
        payoff_bid = []
        for i in range(len(players)):
            for player in players:
                other_player = random.choice(players[:i] + players[i + 1:])
                payoff_bid.append(self.phase_1_3_payoff(player, other_player))

        cutoff_bid = []
        for i in range(len(players)):
            for player in players:
                other_player = random.choice(players[:i] + players[i + 1:])
                cutoff_bid.append(self.phase_2_3_payoff(player, other_player))

        for i in range(len(players)):
            for player in players:
                player.payoff = (float(cutoff_bid[i]) + float(payoff_bid[i])) / 2

    def phase_2_3_payoff(self, player, other):
        player_participant_vars = player.participant.vars
        bid = player_participant_vars['auction_b_id']
        player_auction = player_participant_vars['auctions'][bid]
        cutoff = player_auction.cutoff
        player.cutoff_2 = cutoff
        max_value = player_auction.max_value
        min_value = player_auction.min_value
        r = (max_value - min_value) * random.random() + min_value
        player.random_cutoff_2 = r
        if r >= cutoff:
            return r
        else:
            # Determine if the player wins the auction
            other_participant_vars = other.participant.vars

            player.round_2 = player_participant_vars['round_b']

            aid = player_participant_vars['auction_b_id']
            player.auction_2 = aid

            choice = player_participant_vars['auction_b_id_choice']
            player.choice_2 = choice

            player_auction = player_participant_vars['auctions'][aid]
            other_auction = other_participant_vars['auctions'][aid]

            player_random_signal = player_auction.random_signal
            player.signal_2 = player_random_signal
            other_random_signal = random.choice(player_auction.signals)
            player.other_signal_2 = player_random_signal

            player_bid = player_auction.bids[player_auction.random_signal]
            player.bid_2 = player_bid
            other_bid = other_auction.bids[random.choice(player_auction.signals)]
            player.other_bid_2 = other_bid

            if player_bid == other_bid:
                player_wins = random.randint(0, 1) == 1
            else:
                player_wins = player_bid > other_bid

            player.winner_2 = player_wins

            if not player_wins:
                player.earnings_2 = 0
                return 0
            else:
                low_prob = player_auction.low_probability(player_random_signal, other_random_signal)
                r = random.random()
                player.random_low_prob_2 = r
                if r < low_prob:
                    low_value = player_auction.low_value(player_random_signal, other_random_signal)
                    player.earnings_2 = player_bid + low_value
                    return player_bid + low_value
                else:
                    high_value = player_auction.high_value(player_random_signal, other_random_signal)
                    player.earnings_2 = player_bid + high_value
                    return player_bid + high_value

    def phase_1_3_payoff(self, player, other):
        # Determine if the player wins the auction
        player_participant_vars = player.participant.vars
        other_participant_vars = other.participant.vars

        player.round_1 = player_participant_vars['round_a']

        aid = player_participant_vars['auction_a_id']
        player.auction_1 = aid

        choice = player_participant_vars['auction_a_id_choice']
        player.choice_1 = choice

        player_auction = player_participant_vars['auctions'][aid]
        other_auction = other_participant_vars['auctions'][aid]

        player_random_signal = player_auction.random_signal
        player.signal_1 = player_random_signal
        other_random_signal = random.choice(player_auction.signals)
        player.other_signal_1 = other_random_signal

        player_bid = player_auction.bids[player_auction.random_signal]
        player.bid_1 = player_bid
        other_bid = other_auction.bids[random.choice(player_auction.signals)]
        player.other_bid_1 = other_bid

        if player_bid == other_bid:
            player_wins = random.randint(0, 1) == 1
        else:
            player_wins = player_bid > other_bid

        player.winner_1 = player_wins

        if not player_wins:
            player.earnings_1 = 0
            return 0
        else:
            low_prob = player_auction.low_probability(player_random_signal, other_random_signal)
            r = random.random()
            player.random_low_prob_1 = r
            if r < low_prob:
                low_value = player_auction.low_value(player_random_signal, other_random_signal)
                player.earnings_1 = player_bid + low_value
                return player_bid + low_value
            else:
                high_value = player_auction.high_value(player_random_signal, other_random_signal)
                player.earnings_1 = player_bid + high_value
                return player_bid + high_value


class Results(Page):
    def vars_for_template(self):
        auctions = AuctionCollectionFactory.auctions()
        aid = self.player.participant.vars['auction_a_id']

        return {'auction_1': auctions[aid]}


page_sequence = [
    ResultsWaitPage,
    Results,
]
