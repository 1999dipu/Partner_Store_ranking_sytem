# Generated by Django 3.0.5 on 2020-04-29 07:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0009_auto_20200429_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboard',
            name='zipcode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Only numbers are allowed'), django.core.validators.MinLengthValidator(6)]),
        ),
    ]