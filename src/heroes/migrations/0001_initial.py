# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 16:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('avatar', models.CharField(max_length=500)),
                ('video', models.CharField(max_length=500)),
                ('about', models.CharField(max_length=1000)),
                ('subscribers', models.ManyToManyField(blank=True, related_name='hero_subscribers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hero', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]