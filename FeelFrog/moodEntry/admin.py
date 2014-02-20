from django.contrib import admin
from django.contrib.auth.models import User
from moodEntry.models import *


admin.site.register(Activity)
admin.site.register(Activities)
admin.site.register(MoodAtTime)
admin.site.register(ActivityAtTime)
admin.site.register(ActivityVector)
admin.site.register(MoodPredicted)