from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
  # The custom user model
  user = models.OneToOneField(User)
  name = models.CharField(max_length=30)
  real_name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name

class Activity(models.Model):
  # All possible activities
  name = models.CharField(max_length=200, unique=True)
  userCreated = models.BooleanField()
  user = models.ForeignKey(MyUser)
  no = models.PositiveIntegerField()
  
  def __unicode__(self):
    return self.name

class Activities(models.Model):
  # The user's set of activities
  user = models.ForeignKey(MyUser, unique=True)
  activitys = models.ManyToManyField(Activity, db_index=False)

class MoodAtTime(models.Model):
  # A mood and a time
  mood = models.PositiveIntegerField()
  time = models.DateTimeField()
  user = models.ForeignKey(MyUser)
  
  def __unicode__(self):
    return u'%s %s' % (self.mood, self.time)

  class Meta:
    unique_together = ('time','user')

class ActivityAtTime(models.Model):
  # An activty and a time
  user = models.ForeignKey(MyUser)
  activity = models.ForeignKey(Activity)
  timeStart = models.DateTimeField()
  timeStop = models.DateTimeField()
  
  def __unicode__(self):
    return u'%s %s %s' % (self.activity, self.timeStart, self.timeStop)

  class Meta:
    unique_together = (('timeStart','user'),('timeStop','user'))

  def is_valid(self):
    return self.timeStart < self.timeStop

class ActivityVector(models.Model):
  # Set of activities between mood changes
  vector = models.IntegerField()
  user = models.ForeignKey(MyUser)

  def __unicode__(self):
    return u'%i' % (self.vector)

  def getVec(self):
    vect = []
    for x in range(0, 9):
      vect.append(((self.vector)>>x)%2)
    vect.append(((self.vector)>>10)%8)
    return vect

class MoodPredicted(models.Model):
  moodStart = models.ForeignKey(MoodAtTime, related_name="moodStart")
  moodStop = models.ForeignKey(MoodAtTime, related_name="moodStop")
  activityV = models.ForeignKey(ActivityVector)
  user = models.ForeignKey(MyUser)
  prediction = models.IntegerField()
  fromTime = models.DateTimeField()
  toTime = models.DateTimeField()
