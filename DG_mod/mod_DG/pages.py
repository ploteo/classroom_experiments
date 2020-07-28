from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

#---------------------------------------------------------
#Commented for the Prolific version (comoutations ex-post)
#---------------------------------------------------------
# class ResultsWaitPage(WaitPage):
#     def after_all_players_arrive(self):
#         self.group.set_payoffs_DG()

class Instructions(Page):
    form_model = 'player'
    form_fields = ['C_0']

    import random

    def vars_for_template(self):
        import random
        B=random.randint(0,10)
        return{
        'A_own': 10,
        'A_other': 0,
        'B': B
        }

class MPL(Page):
    form_model = 'player'
    form_fields = ['C_1','C_2','C_3','C_4','C_5','C_6','C_7','C_8','C_9','C_10','C_11']

    def vars_for_template(self):
        B=[]
        for i in range(11):
            B.append(i)
        return{

        'A_own': Constants.A_own,
        'A_other': Constants.A_other,
        'B1':B[0],
        'B2':B[1],
        'B3':B[2],
        'B4':B[3],
        'B5':B[4],
        'B6':B[5],
        'B7':B[6],
        'B8':B[7],
        'B9':B[8],
        'B10':B[9],
        'B11':B[10]
        }

class Results(Page):
    def vars_for_template(self):
        return{
        'type':self.player.type,
        'payoff':self.participant.vars['payoff_DG'],
        'chosen':self.participant.vars['chosen'],
        'choice':self.participant.vars['chosen']
        }


page_sequence = [Instructions, MPL] # Removed  ResultsWaitPage for the Prolific version
