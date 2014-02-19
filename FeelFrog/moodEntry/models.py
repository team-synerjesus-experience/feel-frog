from django.db import models

# Create your models here.

class User(models.Model):
  user = models.CharField(max_length=100,unique=True)
  real_name = models.CharField(max_length=200)

class Activity(models.Model):
  name = models.CharField(max_length=200, unique=True)
  userCreated = models.BooleanField()
  user = models.ForeignKey(User)

class Activities(models.Model):
  user = models.ForeignKey(User, unique=True)
  activitys = models.ManyToManyField(Activity, db_index=False)

class MoodAtTime(models.Model):
  mood = models.PositiveIntegerField()
  time = models.DateTimeField()
  user = models.ForeignKey(User)

  class Meta:
    unique_together = ('time','user')

class ActivityAtTime(models.Model):
  user = models.ForeignKey(User)
  activity = models.ForeignKey(Activity)
  timeStart = models.DateTimeField()
  timeStop = models.DateTimeField()
  
  class Meta:
    unique_together = (('timeStart','user'),('timeStop','user'))

  def is_valid(self):
    return self.timeStart < self.timeStop

class ActivityVector(models.Model):
  vector = models.IntegerField()
  user = models.ForeignKey(User)

class MoodPredicted(models.Model):
  moodStart = models.ForeignKey(MoodAtTime, related_name="moodStart")
  moodStop = models.ForeignKey(MoodAtTime, related_name="moodStop")
  activityV = models.ForeignKey(ActivityVector)
  user = models.ForeignKey(User)
  prediction = models.IntegerField()
  fromTime = models.DateTimeField()
  toTime = models.DateTimeField()
