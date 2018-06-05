from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    age = models.IntegerField(min=18, max=100, blank=False)
    major = models.CharField(max_length=255, blank=False)
    q1 = models.TextField(blank=False)
    q2 = models.TextField(blank=False)
    q3 = models.TextField(blank=False)
    q4 = models.TextField(blank=False)
    q5 = models.TextField(blank=False)
    q6 = models.TextField(blank=False)
