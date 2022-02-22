# Generated by Django 4.0.1 on 2022-02-01 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country_code', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=10)),
                ('career_objective', models.TextField()),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('address', models.TextField()),
                ('hobbies', models.TextField()),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
