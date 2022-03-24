from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question (models.Model):
    question= models.CharField(max_length=130)
    date_question = models.DateField()
    who_make_question = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Answers (models.Model):
    question_solution = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    date_solution = models.DateField()
    who_make_answer = models.ForeignKey(User, on_delete=models.CASCADE)


    
