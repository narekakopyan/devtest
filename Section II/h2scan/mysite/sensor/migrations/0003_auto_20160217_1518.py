# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-02-17 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_auto_20160217_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeSys', models.CharField(max_length=200)),
                ('TimeSec', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PcbAdc', models.IntegerField(default=0)),
                ('TempAdc', models.IntegerField(default=0)),
                ('HCurrent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Res2Adc', models.IntegerField(default=0)),
                ('Res1Adc', models.IntegerField(default=0)),
                ('PcbTemp', models.DecimalField(decimal_places=4, max_digits=6)),
                ('SnsrTemp', models.DecimalField(decimal_places=5, max_digits=7)),
                ('Messages', models.CharField(max_length=200)),
                ('line_number', models.IntegerField(default=0)),
                ('file_name', models.CharField(max_length=200)),
                ('config', models.CharField(max_length=200)),
                ('sensor_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='HCurrent',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Messages',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='PcbAdc',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='PcbTemp',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Res1Adc',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='Res2Adc',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='SnsrTemp',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='TempAdc',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='TimeSec',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='TimeSys',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='config',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='line_number',
        ),
        migrations.AddField(
            model_name='sensordata',
            name='Sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.Sensor'),
        ),
    ]