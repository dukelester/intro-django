import datetime

from django.contrib import admin
from django.utils import timezone

from . import models
# Register your models here.
from .models import Question, Choice


# admin.site.register(Question)
# customizing the admin section
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='Published recently'
    # )
    # def was_published_recent(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'question', 'votes']


# admin.site.register(Choice)
admin.site.register(Choice, ChoiceAdmin)
