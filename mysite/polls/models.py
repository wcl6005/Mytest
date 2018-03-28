# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=200) #作者
    title = models.CharField(max_length=200) #标题

    def __unicode__(self):
        return "%s %s" %(self.author, self.title)