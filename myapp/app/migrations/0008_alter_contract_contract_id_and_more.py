# Generated by Django 4.2.7 on 2023-12-17 04:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_contract_contract_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_id',
            field=models.CharField(default='d1708811', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='jersey_number',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
