from django.shortcuts import render
from leads.models import Lead 
from .serializers import LeadSerializer

# Create your views here.
class LeadView():
    queryset = Lead.object.all()
    serializer_class = LeadSerializer