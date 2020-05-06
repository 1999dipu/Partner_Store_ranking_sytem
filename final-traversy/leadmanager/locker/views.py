from django.shortcuts import render
from .models import Rankinglist
from .serializer import RankingListSerializer
from rest_framework import generics

class RankingListCreate(generics.ListCreateAPIView):
    queryset = Rankinglist.objects.all()
    serializer_class = RankingListSerializer

