# Generated by Django 3.0.6 on 2020-06-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_adda', '0018_subject_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/assignment_adda')),
            ],
        ),
    ]