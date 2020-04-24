from django.urls import path
from . import views

urlpatterns = [
    path('api/onboard/', views.OnboardListCreate.as_view() ),
    path('api/availability/', views.AvailabilityListCreate.as_view() ),
]