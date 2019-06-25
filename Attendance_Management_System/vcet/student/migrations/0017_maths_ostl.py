# Generated by Django 2.0.2 on 2018-04-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20180402_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maths',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('_1', models.CharField(default='Not', max_length=20)),
                ('_2', models.CharField(default='Not', max_length=20)),
                ('_3', models.CharField(default='Not', max_length=20)),
                ('_4', models.CharField(default='Not', max_length=10)),
                ('_5', models.CharField(default='Not', max_length=10)),
                ('_6', models.CharField(default='Not', max_length=10)),
                ('_7', models.CharField(default='Not', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ostl',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('_1', models.CharField(default='Not', max_length=20)),
                ('_2', models.CharField(default='Not', max_length=20)),
                ('_3', models.CharField(default='Not', max_length=20)),
                ('_4', models.CharField(default='Not', max_length=10)),
                ('_5', models.CharField(default='Not', max_length=10)),
                ('_6', models.CharField(default='Not', max_length=10)),
                ('_7', models.CharField(default='Not', max_length=10)),
            ],
        ),
    ]
