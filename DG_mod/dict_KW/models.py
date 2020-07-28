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


author = 'MP'

doc = """
A KW like game on a modified dictator grame (see "mod_DG")
"""


class Constants(BaseConstants):
    name_in_url = 'dict_KW'
    players_per_group = None
    num_rounds = 1
    A_own = 10
    A_other = 0
    payout_KW=5
    import random
    rdm_row = random.randint(0,10)# which choice is chosen, same for all


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoff(self):
        players = self.get_players()
        all_choices = [[p.C_1 for p in players], [p.C_2 for p in players],[p.C_3 for p in players],[p.C_4 for p in players],[p.C_5 for p in players],[p.C_6 for p in players],[p.C_7 for p in players],[p.C_8 for p in players],[p.C_9 for p in players],[p.C_10 for p in players],[p.C_11 for p in players]]
        import collections
        freq=collections.Counter(all_choices[Constants.rdm_row])
        most_common=freq.most_common(1)[0][0]
        print(freq)
        print(most_common)

        for p in players:#to store them across app
            own_choices=[p.C_1,p.C_2,p.C_3,p.C_4,p.C_5,p.C_6,p.C_7,p.C_8,p.C_9,p.C_10,p.C_11]
            if own_choices[Constants.rdm_row]==most_common:
                payoff_KW=Constants.payout_KW
            else:
                payoff_KW=0

            p.participant.vars['payoff_KW']=payoff_KW
            p.participant.vars['own_choice']=own_choices[Constants.rdm_row]
            p.participant.vars['rdm_row']=Constants.rdm_row
            p.participant.vars['most_common']=most_common
            p.payoff=payoff_KW
            p.payoff_TOT=p.participant.vars['payoff_DG']+p.participant.vars['payoff_KW']


class Player(BasePlayer):
    C_0 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']],blank=True)

    payoff_TOT=models.PositiveIntegerField()#to store total payoff

    C_1 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_2 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_3 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_4 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_5 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_6 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_7 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_8 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_9 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_10 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
    C_11 = models.PositiveIntegerField(choices=[[4, 'Very appropriate'],[3, 'Somewhat appropriate'],[2,'Somewhat inappropriate'],[1,'Very inappropriate']])
