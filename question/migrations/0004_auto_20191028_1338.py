# Generated by Django 2.2.6 on 2019-10-28 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20191028_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='thumbs_down',
            field=models.IntegerField(default=0, verbose_name='Num_of_dislikes'),
        ),
        migrations.AddField(
            model_name='question',
            name='thumbs_up',
            field=models.IntegerField(default=0, verbose_name='Num_of_likes'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 10, 28, 13, 38, 10, 467440), verbose_name='Birthday'),
        ),
    ]
