from django.urls import path
from . import views

urlpatterns = [
    path('api/rankinglist/', views.RankingListCreate.as_view() ),
]