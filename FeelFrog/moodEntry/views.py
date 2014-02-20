from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from moodEntry.models import *


if not settings.configured:
	settings.configure(myapp_defaults, DEBUG=True)

def getMood(request):
	latest_mood = MoodAtTime.objects.order_by('-time')[0]
	return HttpResponse("The most recent mood was at %s" % latest_mood)

def activities(request, start, stop):
	act = ActivityAtTime.objects.filter(timeStop__gte=start)
	return HttpResponse("The most recent mood was at %s" % latest_mood)
