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
    name_in_url = 'wikipedia_task'
    players_per_group = None
    num_rounds = 1

    participants_colors = {'Blue': '#0000ff', 'Red': '#ff0000'}

    articles = [
        (t.split(" ")[1], t) for t in
        ['Emmanuel Saez (économiste)', 'Stéphanie Stantcheva (économiste)', 'Fatoumata Kébé (scientifique)',
         'Wendelin Werner (scientifique)', 'Céline Curiol (écrivaine)', 'Dominic Bellavance (écrivain)',
         'Valérie Jouvre (artiste)', 'Quentin Spohn (artiste)']
    ]

    minutes_for_chatting = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    doc_id = models.StringField()
    track_change = models.LongStringField()
    article_edited = models.LongStringField()


class Player(BasePlayer):
    pass
