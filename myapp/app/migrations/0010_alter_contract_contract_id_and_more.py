# Generated by Django 4.2.7 on 2023-12-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_contract_contract_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_id',
            field=models.CharField(default='b0a61e8a', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transfer_amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]