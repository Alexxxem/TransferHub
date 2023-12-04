# Generated by Django 4.2.7 on 2023-12-03 10:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_id',
            field=models.CharField(default='868b246a', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='jersey_number',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
