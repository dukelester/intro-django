from django.contrib import admin

from . import models
# Register your models here.
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)