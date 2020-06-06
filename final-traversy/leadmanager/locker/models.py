from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
# Create your models here.
class Onboard(models.Model):
	lockerid	=models.IntegerField(primary_key=True)
	name		=models.CharField(max_length=250)
	country		=models.CharField(max_length=100,validators=[RegexValidator(r'^[a-zA-Z ]+$',message='Numbers not allowed')],default="India")
	address 	=models.TextField()
	zipcode 	=models.CharField(max_length=6,validators=[RegexValidator(r'^\d{1,10}$',message='Only numbers are allowed'), MinLengthValidator(6)])
	total_slots =models.IntegerField()
	latitude	=models.FloatField(default="0.0000000")
	longitude	=models.FloatField(default="0.0000000")


class Rating(models.Model):
	lockerid	=models.ForeignKey(Onboard, on_delete=models.CASCADE)
	rating      =models.DecimalField(max_digits=2,decimal_places=1, default=2.5)

class Throughput(models.Model):
	lockerid	=models.ForeignKey(Onboard, on_delete=models.CASCADE)
	throughput  =models.FloatField(default=5.6)

class Availability(models.Model):
	lockerid		=models.OneToOneField(Onboard, on_delete=models.CASCADE,primary_key=True)
	non_del_days	=models.CharField('Non delivery days',max_length=7,default='0000000',validators=[RegexValidator(r'^\d{1,10}$',message='Letters not permissible'),MinLengthValidator(7)])
	timings_open 	=models.TimeField(default="07:00")
	timings_closed 	=models.TimeField(default="22:00")
	status			=models.BooleanField(default=True)

class Occupancy(models.Model):
	lockerid		=models.ForeignKey(Onboard, on_delete=models.CASCADE)
	date			=models.DateField(default=timezone.now)
	occupancy		=models.FloatField(default=2)	
	class Meta:
		unique_together=('lockerid','date')

class Rankinglist(models.Model):
	lockerid		=models.ForeignKey(Onboard, on_delete=models.CASCADE)
	rank 			=models.IntegerField()
	name			=models.CharField(max_length=250,validators=[RegexValidator(r'^[a-zA-Z ]+$',message='Numbers not allowed')])
	country			=models.CharField(max_length=100,validators=[RegexValidator(r'^[a-zA-Z ]+$',message='Numbers not allowed')])
	address 		=models.TextField()
	zipcode 		=models.CharField(max_length=6,validators=[RegexValidator(r'^\d{1,10}$',message='Only numbers are allowed'), MinLengthValidator(6)])
	non_del_days	=models.CharField('Non delivery days',max_length=7,default='0000000',validators=[RegexValidator(r'^\d{1,10}$',message='Letters not permissible'),MinLengthValidator(7)])
	timings_open 	=models.TimeField()
	timings_closed 	=models.TimeField()
	status			=models.BooleanField()
	dist            =models.FloatField(default=0.0)
	score           =models.FloatField(default=0.0)
	class Meta:
		unique_together=('lockerid','rank')

