from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question


# Create your tests here.

class QuestionModelTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

    def test_was_published_old_question(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.published_recently(), False)

    def was_published_new_question(self):
        time = timezone.now() + datetime.timedelta(hours=23,minutes=59, seconds=50)
        new_question = Question(pub_date=time)
        self.assertIs(new_question.published_recently(), True)

