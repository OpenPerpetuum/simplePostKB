# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-30 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttackDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage', models.FloatField()),
                ('killing_blow', models.BooleanField()),
                ('ecm_hits', models.PositiveSmallIntegerField()),
                ('ecm_attempts', models.PositiveSmallIntegerField()),
                ('demob', models.PositiveSmallIntegerField()),
                ('suppress', models.PositiveSmallIntegerField()),
                ('energy', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('attackers', models.ManyToManyField(to='kbsite.AttackDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Kill_PureText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('corp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbsite.Corp')),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='kill',
            name='victim_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbsite.Player'),
        ),
        migrations.AddField(
            model_name='kill',
            name='victim_robot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbsite.Robot'),
        ),
        migrations.AddField(
            model_name='kill',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbsite.Zone'),
        ),
        migrations.AddField(
            model_name='attackdetails',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbsite.Player'),
        ),
        migrations.AddField(
            model_name='attackdetails',
            name='robot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kbsite.Robot'),
        ),
    ]
