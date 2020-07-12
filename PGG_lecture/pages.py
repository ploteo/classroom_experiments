from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return{
        'treatment': self.session.config['treatment'],
        'common_proj': Constants.endowment*Constants.players_per_group
        }


class Contribute(Page):
    form_model = 'player'
    form_fields = ['choice']
    #the player will fill out the field choice and it will be saved in player model (see models)

    def vars_for_template(self):
        return{
        'round_number':self.round_number,
        'treatment': self.session.config['treatment'],
        'endowment': Constants.endowment
        }

class ResultsWaitPage(WaitPage):
    #If you have a WaitPage in your sequence of pages, then oTree waits until all players in the group have arrived at that point in the sequence, and then all players are allowed to proceed.
    after_all_players_arrive = 'set_payoffs'
    # see method 'set_payoffs' in class Group in models.py
    # payoffs are computed here

class Results(Page):
    def vars_for_template(self):
        return{
        'round_number':self.round_number,
        'treatment': self.session.config['treatment'],
        }

class FinalResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return{
        'final_payoff':self.player.participant.payoff # from player to participant we get the total earnings cumulative
        }


page_sequence = [Instructions, Contribute, ResultsWaitPage, Results, FinalResults]
