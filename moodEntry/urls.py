from django.conf.urls import patterns, url

from moodEntry import views

urlpatterns = patterns('',
	url(r'^mood/$', views.getMood, name='mood'),
#	url(r'^activities/(?P<start>\d+)/$', views.detail, name='activities'),
)