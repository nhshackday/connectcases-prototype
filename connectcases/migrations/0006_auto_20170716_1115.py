# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectcases', '0005_auto_20170716_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='lower_colet_from',
            field=models.CharField(blank=True, choices=[(b'lower_right_1', b'RIGHT 1'), (b'lower_right_2', b'RIGHT 2'), (b'lower_right_3', b'RIGHT 3'), (b'lower_right_4', b'RIGHT 4'), (b'lower_right_5', b'RIGHT 5'), (b'lower_right_6', b'RIGHT 6'), (b'lower_right_7', b'RIGHT 7')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='lower_colet_to',
            field=models.CharField(blank=True, choices=[(b'lower_left_1', b'LEFT 1'), (b'lower_left_2', b'LEFT 2'), (b'lower_left_3', b'LEFT 3'), (b'lower_left_4', b'LEFT 4'), (b'lower_left_5', b'LEFT 5'), (b'lower_left_6', b'LEFT 6'), (b'lower_left_7', b'LEFT 7')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='upper_colet_from',
            field=models.CharField(blank=True, choices=[(b'upper_right_1', b'RIGHT 1'), (b'upper_right_2', b'RIGHT 2'), (b'upper_right_3', b'RIGHT 3'), (b'upper_right_4', b'RIGHT 4'), (b'upper_right_5', b'RIGHT 5'), (b'upper_right_6', b'RIGHT 6'), (b'upper_right_7', b'RIGHT 7')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='upper_colet_to',
            field=models.CharField(blank=True, choices=[(b'upper_left_1', b'LEFT 1'), (b'upper_left_2', b'LEFT 2'), (b'upper_left_3', b'LEFT 3'), (b'upper_left_4', b'LEFT 4'), (b'upper_left_5', b'LEFT 5'), (b'upper_left_6', b'LEFT 6'), (b'upper_left_7', b'LEFT 7')], max_length=13, null=True),
        ),
    ]