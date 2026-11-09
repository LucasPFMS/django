from django.db import models
import datetime
# Create your models here.
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __repr__(self):
        return "<Question: {}>".format(self.question_text)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def get_choices(self):
    total = 0
    choices = self.choice_set.all()
    for c in choices:
        total += c.votes
    return [(c.choice_text, c.votes, c.votes / total) for c in choices]