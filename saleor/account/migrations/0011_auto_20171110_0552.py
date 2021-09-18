# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("account", "0010_auto_20170919_0839")]

    replaces = [("userprofile", "0011_auto_20171110_0552")]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": (
                    ("view_user", "Can view users"),
                    ("edit_user", "Can edit users"),
                    ("view_group", "Can view groups"),
                    ("edit_group", "Can edit groups"),
                    ("view_staff", "Can view staff"),
                    ("edit_staff", "Can edit staff"),
                ),
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        )
    ]
