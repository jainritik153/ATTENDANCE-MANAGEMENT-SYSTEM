# Generated by Django 2.0.2 on 2018-03-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20180330_0607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='Null', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='teacherreg',
            name='subject',
            field=models.CharField(default='NULL', max_length=20),
        ),
    ]
