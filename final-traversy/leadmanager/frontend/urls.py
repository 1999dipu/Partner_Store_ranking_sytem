
from django.urls import path
from . import views
urlpatterns = [
  path('', views.index),
  path('listview/', views.index),
  path('onboard/', views.index),
  path('api/onboard/', views.index),
  path('api/leads/', views.index)
]