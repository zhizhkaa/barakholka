# Generated by Django 4.1.7 on 2023-03-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=5),
        ),
    ]
