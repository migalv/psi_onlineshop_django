# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-30 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20171030_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='proName',
            new_name='prodName',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='proSlug',
            new_name='prodSlug',
        ),
    ]