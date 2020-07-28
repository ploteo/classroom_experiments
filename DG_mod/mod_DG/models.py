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
A modified DG, following Blanco, Mariana, Dirk Engelmann, and Hans Theo Normann. "A within-subject analysis of other-regarding preferences." Games and Economic Behavior 72, no. 2 (2011): 321-338.
Needed during lectures. Relevant data are stored to be used across app (possible to join with other apps)
"""


class Constants(BaseConstants):
    name_in_url = 'mod_DG'
    players_per_group = None # usually is 2, modified for prolific
    num_rounds = 1
    A_own = 10
    A_other = 0
    payout_KW=5

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for g in self.get_groups():
            for p in g.get_players():
                if p.id_in_group == 1:
                    p.participant.vars['type'] = 'Dictator'
                else:
                    p.participant.vars['type'] = 'Recipient'
                p.type = p.participant.vars['type']

class Group(BaseGroup):
    # payoff modified DG

    def set_payoffs_DG(self):
        import random
        rdm=random.randint(0,11)#random row
        print(rdm)
        dictator = self.get_player_by_id(1)#use the id in group to get the role (must match subsession)
        recipient = self.get_player_by_id(2)
        choices = [
        dictator.C_1,
        dictator.C_2,
        dictator.C_3,
        dictator.C_4,
        dictator.C_5,
        dictator.C_6,
        dictator.C_7,
        dictator.C_8,
        dictator.C_9,
        dictator.C_10,
        dictator.C_11
        ]
        if choices[rdm]==1:#A
            dictator.participant.vars['payoff_DG']=10
            recipient.participant.vars['payoff_DG']=0
            dictator.participant.vars['choice']="A"
            recipient.participant.vars['choice']="A"
        else:
            dictator.participant.vars['payoff_DG']=rdm
            recipient.participant.vars['payoff_DG']=rdm
            dictator.participant.vars['choice']="B"
            recipient.participant.vars['choice']="B"
        #common to both players
        dictator.participant.vars['chosen']=rdm
        recipient.participant.vars['chosen']=rdm
        players = self.get_players()
        for p in players:
            p.payoff=p.participant.vars['payoff_DG']

class Player(BasePlayer):
    type = models.StringField()
    chosen= models.PositiveIntegerField()
    choice= models.StringField()

    C_0=models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],blank=True,widget=widgets.RadioSelectHorizontal)

    # This is for main choices, each variable is one row in the choice table MPL
    C_1 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_2 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_3 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_4 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_5 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_6 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_7 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_8 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_9 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_10 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    C_11 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
