# Generated by Django 5.0.4 on 2024-04-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_complaints_date_restoration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='description_failure',
            field=models.TextField(verbose_name='Описание отказа'),
        ),
    ]
