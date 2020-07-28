from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class AnagQuest(Page):
    form_model = 'player'
    form_fields = ['sex','age','residence','comment']


page_sequence = [AnagQuest]
