from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
  url(r'^$', views.QuestionList.as_view(), name='question_list'),
 # url(r'^question/(?P<pk>\d+)$', views.QuestionDetail.as_view(), name='question_detail'),
  url(r'^new$', views.QuestionCreate.as_view(), name='question_new'),
  url(r'^edit/(?P<pk>\d+)$', views.QuestionUpdate.as_view(), name='question_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.QuestionDelete.as_view(), name='question_delete'),
)


