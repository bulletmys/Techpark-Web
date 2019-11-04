# Generated by Django 2.2.6 on 2019-11-03 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_auto_20191103_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ManyToManyField(blank=True, related_name='answers', to='question.Question'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 11, 3, 15, 3, 55, 943262), verbose_name='Birthday'),
        ),
    ]
