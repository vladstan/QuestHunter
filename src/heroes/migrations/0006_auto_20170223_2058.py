# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 20:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heroes', '0005_mydestination'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroTip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.FileField(default='/media/posts/iceland.jpg', upload_to='posts')),
            ],
        ),
        migrations.RenameModel(
            old_name='MyDestination',
            new_name='HeroDestination',
        ),
        migrations.AddField(
            model_name='herotip',
            name='my_destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heroes.HeroDestination'),
        ),
        migrations.AddField(
            model_name='herotip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]