from django.conf.urls import url

from . import views

app_name = 'eightball'
urlpatterns = [
    # ex: /eightball/
    url(r'^$', views.index, name='index'),
    # ex: /eightball/anwser
    url(r'^anwser/$', views.anwser, name='anwser'),
]