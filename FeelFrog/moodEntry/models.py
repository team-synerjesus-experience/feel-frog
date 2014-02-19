from django.db import models

# Create your models here.

class Activity(models.Model):
  name = models.CharField(max_length=200, unique=True)
  userCreated = models.BooleanField()
  user = models.CharField(max_length=100)

class Activities(models.Model):
  user=models.CharField(max_length=100,unique=True)
  activity1 = models.ManyToManyField(Activity, db_index=False)

  

