# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import connection

from django.contrib.auth.models import User

'''
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа
'''

#----------------------------------------------------------------------------------------------
# Question Manager
'''
QuestionManager - менеджер модели Question
new - метод возвращающий последние добавленные вопросы
popular - метод возвращающий вопросы отсортированные по рейтингу
'''
class QuestionManager(models.Manager):
    def new(self):
        return self.orderby('-added_at')
    def popular(self):
        return self.orderby('-rating')


# Create your models here.
#----------------------------------------------------------------------------------------------
# Question
class Question(models.Model):
    title    = models.CharField(max_length=255)
    text     = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating   = models.IntegerField()
    author   = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes    = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    objects = QuestionManager()


#----------------------------------------------------------------------------------------------
# Answer
class Answer(models.Model):
    text     = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author   = models.ForeignKey(User, on_delete=models.DO_NOTHING)


#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
