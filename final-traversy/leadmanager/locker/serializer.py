from rest_framework import serializers
from .models import Rankinglist

class RankingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rankinglist
        fields = '__all__'

