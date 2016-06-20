from django.db import models

class Table(models.Model):
    target = models.CharField(max_length=200)
    count = models.PositiveIntegerField()
    days_back = models.PositiveIntegerField(default = 1)

class Days(models.Model):
    days = models.IntegerField()




