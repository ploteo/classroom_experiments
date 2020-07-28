from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency
)


doc = """
a.k.a. Keynesian beauty contest.

Players all guess a number; whoever guesses closest to
2/3 of the average wins.
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 3
    name_in_url = 'beauty_contest'

    jackpot = Currency(100)
    guess_max = 100

    instructions_template = 'beauty_contest/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():# copy the treatment for each subject
            if self.round_number == 1:
                p.participant.vars['total_payoff']=0
            if p.id_in_group % 2 == 0:
                p.display="slider_100"
            else:
                p.display="slider_0"


class Group(BaseGroup):
    two_thirds_avg = models.FloatField()
    best_guess = models.PositiveIntegerField()
    num_winners = models.PositiveIntegerField()

    def set_payoffs(self):
        players = self.get_players()
        guesses = [p.guess for p in players]
        two_thirds_avg = (2 / 3) * sum(guesses) / len(players)
        self.two_thirds_avg = round(two_thirds_avg, 2)

        self.best_guess = min(guesses,
            key=lambda guess: abs(guess - self.two_thirds_avg))

        winners = [p for p in players if p.guess == self.best_guess]
        self.num_winners = len(winners)

        for p in winners:
            p.is_winner = True
            p.payoff = Constants.jackpot / self.num_winners

        for p in self.get_players():
            p.participant.vars['total_payoff']=p.participant.vars['total_payoff']+p.payoff
            p.total_payoff=p.participant.vars['total_payoff']

    def two_thirds_avg_history(self):
        return [g.two_thirds_avg for g in self.in_previous_rounds()]


class Player(BasePlayer):
    guess = models.PositiveIntegerField(max=Constants.guess_max)
    is_winner = models.BooleanField(initial=False)
    total_payoff=models.CurrencyField()
    display=models.CharField()
