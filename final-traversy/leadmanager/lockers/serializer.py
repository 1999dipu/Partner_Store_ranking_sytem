from rest_framework import serializers
from .models import Onboard
from .models import Availability

class LockerOnboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboard
        fields = ('lockerid','name','country','address','zipcode')

class LockerAvailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ('lockerid','non_del_days','timings_open','timings_closed','status')
