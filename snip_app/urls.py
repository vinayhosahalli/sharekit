from django.conf.urls import url
from django.urls import path
from snip_app import views
import uuid

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('show_snips/<uuid:pk>/', views.show_snip, name='show_snips'),
]
