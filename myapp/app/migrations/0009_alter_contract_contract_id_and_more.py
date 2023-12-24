# Generated by Django 4.2.7 on 2023-12-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_contract_contract_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_id',
            field=models.CharField(default='fa8718c8', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_type',
            field=models.CharField(choices=[('standard', 'Стандартный'), ('rental', 'Аренда')], max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('GOALKEEPER', 'Вратарь'), ('DEFENDER', 'Защитник'), ('MIDFIELDER', 'Полузащитник'), ('FORWARD', 'Нападающий')], max_length=20),
        ),
    ]
