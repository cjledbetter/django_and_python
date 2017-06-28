# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.TextField(max_length=254)
	body = models.TextField()
	likes = models.IntegerField()

class Comment(models.Model):
	article = models.ForeignKey(Article)
	text = models.TextField()
	
