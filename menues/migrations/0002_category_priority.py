# Generated by Django 3.1.2 on 2020-10-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
