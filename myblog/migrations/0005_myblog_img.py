# Generated by Django 3.0.6 on 2020-06-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20200627_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='img',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
