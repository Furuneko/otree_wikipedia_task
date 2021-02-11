from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from django.template.loader import render_to_string


class Task(Page):
    form_model = 'group'
    form_fields = ['article_edited']

    def vars_for_template(self):
        channel_name = f'{self.session.code}_{self.group.id_in_subsession}'
        article = render_to_string('wikipedia_task/articles/' + 'Saez' + '.html')
        doc_id = 'id'
        return dict(channel_name=channel_name, article=article, doc_id=doc_id)


page_sequence = [Task]
