from . import models
from ._builtin import Page, WaitPage


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Guess2(Page):
    form_model = models.Player
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        sorted_guesses = sorted(p.guess for p in self.group.get_players())
        return {'sorted_guesses': sorted_guesses}

class FinalResults(Page):
    def vars_for_template(self):
        return {'total_payoff': self.player.total_payoff}

    def is_displayed(self):
        return self.round_number == 3

page_sequence = [Instructions, Guess2, ResultsWaitPage, Results, FinalResults]
