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

class Constants(BaseConstants):
    name_in_url = 'PGG'
    players_per_group = 4
    num_rounds = 5

    endowment = c(100)
    multiplier = 2

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1: # this way we get a fixed role across repetitions
            self.group_randomly()
        else:
            self.group_like_round(1)

        for p in self.get_players():# copy the treatment for each subject
            p.treatment=self.session.config['treatment']


class Group(BaseGroup):
    total_choices = models.CurrencyField() # for VC is withdrawals, for CP is contributions

    individual_share = models.CurrencyField()
    total_earnings = models.CurrencyField()

    def set_payoffs(self):
        players = self.get_players()
        choices = [p.choice for p in players]
        self.total_choices = sum(choices)
        if self.session.config['treatment'] == "VC":
            self.total_earnings = self.total_choices * Constants.multiplier
            self.individual_share = (
                self.total_earnings / Constants.players_per_group
            )
            for p in players:
                p.payoff = Constants.endowment - p.choice + self.individual_share
        else: # treatment CP
            self.total_earnings = ((Constants.endowment*Constants.players_per_group)-self.total_choices) * Constants.multiplier
            self.individual_share = (
                self.total_earnings / Constants.players_per_group
            )
            for p in players:
                p.payoff =  p.choice + self.individual_share

class Player(BasePlayer):
    choice = models.CurrencyField(min=0,max=Constants.endowment)#
    # for VC is withdrawals, for CP is contributions
    treatment=models.CharField()
    # copy the treatment, mainly for data analysis
