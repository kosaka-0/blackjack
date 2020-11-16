from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^card/$', views.card),
    url(r'^welcome/$', views.welcome),
    url(r'^cards/$', views.cards),
    url(r'^random_cards/$', views.random_cards),
    url(r'^form_test/$', views.form_test),
    url(r'^form_card/$', views.form_card),
    url(r'^login/$', views.login),
]