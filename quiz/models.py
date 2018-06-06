from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Q1_CHOICES = (
        (1, 'The higher bidder always get positive earnings.'),
        (2, 'The higher bidder always gets higher earnings than the low bidder.'),
        (3, 'The low bidder always get 0.')
    )
    Q2_CHOICES = (
        (1, 'The high credit amount in the lottery minus your bid.'),
        (2, 'The outcome of the lottery (random realization) minus your bid.'),
    )
    Q3_CHOICES = (
        (1, 'Both of you get the outcome of the lottery.'),
        (2, 'Both of you get 0.'),
        (3, 'You get the outcome of the lottery with a 50% chance.')
    )
    Q4_CHOICES = (
        (1, '$1.5 - $1 = $0.5'),
        (2, '$1.5'),
        (3, '$0'),
    )
    Q5_CHOICES = (
        (1, 'You have to pay $1 to participate in the auction.'),
        (2, 'You have to pay $1 and you do not participate in the auction.'),
        (3, 'You receive $2 and you do not participate in the auction.')
    )
    Q6_CHOICES = (
        (1, '$2 (= [2+2]/2)'),
        (2, '$2.5 (= [2+3]/2)'),
        (3, '$3 (= [2+4]/2)'),
        (4, '$4 (= [4+4]/2)'),
    )

    q1 = models.IntegerField(label='', choices=Q1_CHOICES, widget=widgets.RadioSelect, blank=False)
    q2 = models.IntegerField(label='', choices=Q2_CHOICES, widget=widgets.RadioSelect, blank=False)
    q3 = models.IntegerField(label='', choices=Q3_CHOICES, widget=widgets.RadioSelect, blank=False)
    q4 = models.IntegerField(label='', choices=Q4_CHOICES, widget=widgets.RadioSelect, blank=False)
    q5 = models.IntegerField(label='', choices=Q5_CHOICES, widget=widgets.RadioSelect, blank=False)
    q6 = models.IntegerField(label='', choices=Q6_CHOICES, widget=widgets.CheckboxInput,
                             blank=False)
