# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name=b'title')),
                ('description', models.CharField(max_length=1000, verbose_name=b'description')),
                ('client', models.CharField(max_length=100, verbose_name=b'client_name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=b'title')),
                ('description', models.CharField(max_length=1000, verbose_name=b'description')),
                ('time_elasped', models.IntegerField(blank=True, default=None, null=True, verbose_name=b'time_elasped')),
                ('importance', models.IntegerField(verbose_name=b'importance')),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Project', verbose_name=b'project')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name=b'name')),
                ('login', models.CharField(max_length=20, verbose_name=b'login')),
                ('password', models.CharField(max_length=20, verbose_name=b'password')),
                ('phone', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name=b'phone')),
                ('born_date', models.DateField(blank=True, default=None, null=True, verbose_name=b'born_date')),
                ('last_connection', models.DateTimeField(blank=True, default=None, null=True, verbose_name=b'date of last connection')),
                ('email', models.EmailField(max_length=254, verbose_name=b'email')),
                ('years_seniority', models.IntegerField(verbose_name=b'senerioity')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name=b'user_created_date')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taskmanager.UserProfile')),
            ],
            bases=('taskmanager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taskmanager.UserProfile')),
                ('specialization', models.CharField(max_length=50, verbose_name=b'specialization')),
            ],
            bases=('taskmanager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ManyToManyField(to='taskmanager.Developer', verbose_name=b'developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Supervisor', verbose_name=b'supervisor'),
        ),
    ]