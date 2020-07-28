from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'demo_questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sex = models.CharField(widget=widgets.RadioSelectHorizontal(),choices=['Male', 'Female'])
    age = models.IntegerField(choices = range(18,100,1))
    comment = models.StringField(blank=True)
    residence = models.CharField()
