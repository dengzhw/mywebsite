# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField(db_column='pub_date')),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('hcontent', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo')),
            ],
        ),
    ]
