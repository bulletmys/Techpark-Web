# Generated by Django 2.2.6 on 2019-10-31 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20191028_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='amount',
            field=models.IntegerField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 16, 33, 22, 498965), verbose_name='Birthday'),
        ),
    ]
