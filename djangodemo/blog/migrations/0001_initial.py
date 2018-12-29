# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertReport',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('alert_from', models.IntegerField(default=1, verbose_name=b'\xe5\x91\x8a\xe8\xad\xa6\xe6\x9d\xa5\xe6\xba\x90')),
                ('from_place', models.CharField(max_length=50, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\x9c\xb0\xe5\xb8\x82')),
                ('from_system', models.CharField(max_length=50, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('from_role', models.CharField(max_length=50, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe8\xa7\x92\xe8\x89\xb2', blank=True)),
                ('from_machine', models.CharField(max_length=50, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe5\x99\xa8', blank=True)),
                ('from_plugin', models.CharField(max_length=30, verbose_name=b'\xe6\x8f\x92\xe4\xbb\xb6', blank=True)),
                ('from_check_method', models.CharField(max_length=100, verbose_name=b'\xe6\xa3\x80\xe6\x9f\xa5\xe9\xa1\xb9', blank=True)),
                ('alert_title', models.CharField(max_length=50, verbose_name=b'\xe5\x91\x8a\xe8\xad\xa6\xe6\xa0\x87\xe9\xa2\x98')),
                ('level', models.IntegerField(default=1, verbose_name=b'\xe5\x91\x8a\xe8\xad\xa6\xe7\xba\xa7\xe5\x88\xab', choices=[(1, b'\xe9\x94\x99\xe8\xaf\xaf\xef\xbc\x88\xe5\xa4\xb1\xe8\xb4\xa5\xef\xbc\x89'), (2, b'\xe8\xad\xa6\xe5\x91\x8a')])),
                ('message', models.TextField(verbose_name=b'\xe5\x91\x8a\xe8\xad\xa6\xe4\xbf\xa1\xe6\x81\xaf', blank=True)),
                ('remark', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('report_time', models.DateTimeField(verbose_name=b'\xe4\xb8\x8a\xe6\x8a\xa5\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xbe\x85\xe5\xa4\x84\xe7\x90\x86'), (1, b'\xe5\xb7\xb2\xe5\xa4\x84\xe7\x90\x86')])),
            ],
            options={
                'verbose_name': '\u544a\u8b66\u4fe1\u606f\u4e0a\u62a5',
                'verbose_name_plural': '\u544a\u8b66\u4fe1\u606f\u4e0a\u62a5',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
