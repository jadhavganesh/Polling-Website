from django.conf.urls import url

from poll import views

urlpatterns = [
	#/poll/vote/1
    url(r'^vote/(?P<poll_pk>\d+)/$', views.vote, name='poll_ajax_vote'),
    #/poll/poll/1
    url(r'^(?P<poll_pk>\d+)/$', views.poll, name='poll'),
    #/poll/result/1
    url(r'^result/(?P<poll_pk>\d+)/$', views.result, name='poll_result'),

    #/poll/thank
    url(r'^thank/$', views.thank, name='poll_thank'),
  
]
