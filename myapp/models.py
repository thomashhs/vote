from django.db import models

# Create your models here.
class Question(models.Model):
    q_text=models.CharField(max_length=200)
    q_date=models.DateTimeField('Date Published')

    def __str__(self):
        return self.q_text

class Choice(models.Model):
    c_question=models.ForeignKey(Question)
    c_text=models.CharField(max_length=200)
    c_votes=models.IntegerField(default=0)

    def __str__(self):
        return self.c_text
