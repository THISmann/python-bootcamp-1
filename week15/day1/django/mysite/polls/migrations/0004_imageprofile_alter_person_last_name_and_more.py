# Generated by Django 4.0.5 on 2022-07-01 04:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProfile',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.person')),
                ('image', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 1, 4, 3, 6, 510944)),
        ),
    ]