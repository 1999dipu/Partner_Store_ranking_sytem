from django.shortcuts import render

from .models import Onboard
from .models import Availability
from .serializer import LockerOnboardSerializer
from .serializer import LockerAvailSerializer
from rest_framework import generics

class OnboardListCreate(generics.ListCreateAPIView):
    queryset = Onboard.objects.all()
    serializer_class = LockerOnboardSerializer

class AvailabilityListCreate(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = LockerAvailSerializer