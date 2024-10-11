# Generated by Django 5.1.2 on 2024-10-11 06:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
