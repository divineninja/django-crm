# polls/models.py
from django.db import models
from ckeditor.fields import RichTextField


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    question_text = RichTextField()
    question_code = models.CharField(max_length=50, unique=True)
    choices = models.ManyToManyField(Choice)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_code


class Campaign(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    campaign_code = models.CharField(max_length=50, unique=True)
    campaign_name = models.CharField(max_length=250)
    questions = models.ManyToManyField(Question)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.campaign_name


class Condition(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='conditions')
    parent_question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='dependent_conditions')
    parent_answer = models.ManyToManyField(Choice)

    def __str__(self):
        return f"{self.question} depends on {self.parent_question}"

