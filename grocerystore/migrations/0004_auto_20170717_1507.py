# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocerystore', '0003_auto_20170717_1432'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductPurchase',
            new_name='ProductPurchaseHistory',
        ),
    ]
