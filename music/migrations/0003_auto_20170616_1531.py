# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_in_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='in_favorite',
            new_name='is_favorite',
        ),
    ]
