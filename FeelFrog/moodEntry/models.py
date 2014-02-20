from django.db import models
from django.contrib.auth.models import User


#class MyUser(models.Model):
  # The custom user model
#  user = models.OneToOneField(User)
# name = models.CharField(max_length=30)
#  real_name = models.CharField(max_length=50)

#  def __unicode__(self):
#    return self.name

class Activity(models.Model):
  # All possible activities
  name = models.CharField(max_length=200, unique=True)
  userCreated = models.BooleanField(default=True)
  user = models.ForeignKey(User)
  no = models.PositiveIntegerField()

  def __unicode__(self):
    return self.name

class Activities(models.Model):
  # The user's set of activities
  user = models.ForeignKey(User, unique=True)
  activitys = models.ManyToManyField(Activity, db_index=False)

class MoodAtTime(models.Model):
  # A mood and a time
  mood = models.PositiveIntegerField()
  time = models.DateTimeField()
  user = models.ForeignKey(User)
  
  def __unicode__(self):
    return u'%s %s' % (self.mood, self.time)

  class Meta:
    unique_together = ('time','user')

class ActivityAtTime(models.Model):
  # An activty and a time
  user = models.ForeignKey(User)
  activity = models.ForeignKey(Activity)
  timeStart = models.DateTimeField()
  timeStop = models.DateTimeField()
  description = models.CharField(max_length=200, null=True, blank=True)
  
  def __unicode__(self):
    return u'%s %s %s' % (self.activity, self.timeStart, self.timeStop)

  class Meta:
    unique_together = (('timeStart','user'),('timeStop','user'))

  def is_valid(self):
    return self.timeStart < self.timeStop

class ActivityVector(models.Model):
  # Set of activities between mood changes
  vector = models.IntegerField()
  user = models.ForeignKey(User)

  def __unicode__(self):
    return u'%i' % (self.vector)


class MoodPredicted(models.Model):
  moodStart = models.ForeignKey(MoodAtTime, related_name="moodStart")
  moodStop = models.ForeignKey(MoodAtTime, related_name="moodStop")
  activityV = models.ForeignKey(ActivityVector)
  user = models.ForeignKey(User)
  prediction = models.IntegerField()
  fromTime = models.DateTimeField()
  toTime = models.DateTimeField()
