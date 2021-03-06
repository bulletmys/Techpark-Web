# Generated by Django 2.2.6 on 2019-11-03 14:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_auto_20191031_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='amount',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 11, 3, 14, 49, 6, 610069), verbose_name='Birthday'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('is_correct', models.BooleanField(default=False)),
                ('datetime_published', models.DateTimeField(verbose_name='Published Date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.User', verbose_name='User')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question', verbose_name='Question')),
            ],
        ),
    ]
