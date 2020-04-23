from django.db import models

# Create your models here.
class Onboard(models.Model):
	lockerid	=models.IntegerField(primary_key=True)
	name		=models.CharField(max_length=250)
	country		=models.CharField(max_length=100)
	address 	=models.TextField()
	zipcode 	=models.IntegerField()
	total_slots =models.IntegerField()

class Rating(models.Model):
	lockerid	=models.IntegerField(primary_key=True)
	rating      =models.DecimalField(max_digits=2,decimal_places=1)

class Throughput(models.Model):
	lockerid	=models.IntegerField(primary_key=True)
	throughput  =models.FloatField()

class Availability(models.Model):
	lockerid		=models.IntegerField(primary_key=True)
	non_del_days	=models.CharField('Non delivery days',max_length=7,default='0000000')
	timings_open 	=models.TimeField()
	timings_closed 	=models.TimeField()
	status			=models.BooleanField()

class Occupancy(models.Model):
	lockerid		=models.IntegerField()
	date			=models.DateField()
	occupancy		=models.FloatField()	
	class Meta:
		unique_together=('lockerid','date')
