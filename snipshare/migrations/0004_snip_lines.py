# Generated by Django 3.0.6 on 2020-06-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snipshare', '0003_auto_20200629_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='snip',
            name='lines',
            field=models.BooleanField(default=False),
        ),
    ]