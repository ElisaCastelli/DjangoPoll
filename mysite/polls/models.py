import datetime

from django.db import models
from django.utils import timezone

# THIS IS THE DATABASE LAYOUT
# Create your models here.

# each model is represented by a class that subclasses django.db.models.Model.
# Each model has a number of class variables, each of which represents a database field in the model.
# Each field is represented by an instance of a Field class that tells Django what type of data each field holds
# Some Field classes have required arguments. CharField, for example, requires that you give it a max_length.
# A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.
# Relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question.


# Django is able to:
#
# Create a database schema (CREATE TABLE statements) for this app.
# Create a Python database-access API for accessing Question and Choice objects.

# three-step guide to making model changes:
#
# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

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
