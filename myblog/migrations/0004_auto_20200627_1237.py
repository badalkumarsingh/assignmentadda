# Generated by Django 3.0.6 on 2020-06-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20200625_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='content',
            field=models.TextField(),
        ),
    ]