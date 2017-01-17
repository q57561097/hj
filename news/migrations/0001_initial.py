# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articl',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('slug', models.CharField(verbose_name='网址', max_length=100, db_index=True)),
                ('content', models.TextField(verbose_name='内容', blank=True, default='')),
                ('pub_date', models.DateTimeField(verbose_name='发表时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now=True)),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('author', models.ForeignKey(verbose_name='作者', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '教程2',
                'verbose_name': '教程1',
            },
        ),
        migrations.CreateModel(
            name='Colum',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='栏目名称', max_length=100)),
                ('slug', models.CharField(verbose_name='栏目网址', max_length=100, db_index=True)),
                ('intro', models.TextField(verbose_name='栏目简介', blank=True, default='')),
                ('nav_display', models.BooleanField(verbose_name='导航显示', default=False)),
                ('home_display', models.BooleanField(verbose_name='首页显示', default=False)),
            ],
            options={
                'verbose_name_plural': '栏目2',
                'ordering': ['name'],
                'verbose_name': '栏目1',
            },
        ),
        migrations.AddField(
            model_name='articl',
            name='column',
            field=models.ManyToManyField(verbose_name='归属栏目', to='news.Colum'),
        ),
    ]
