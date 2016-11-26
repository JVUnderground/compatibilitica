from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question)
    social = models.FloatField(blank=False)
    economic = models.FloatField(blank=False)

    def __str__(self):
        return self.question.title