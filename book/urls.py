from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^postTest/$', postTest, name='postTest'),
    url(r'^postTest1/$', postTest1, name='postTest1'),

]
