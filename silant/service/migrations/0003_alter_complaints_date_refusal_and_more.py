# Generated by Django 5.0.4 on 2024-04-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_complaints_date_refusal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='date_refusal',
            field=models.DateField(verbose_name='Дата отказа'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='date_restoration',
            field=models.DateField(blank=True, null=True, verbose_name='Дата восстановления'),
        ),
    ]
