# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 05:39
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_auto_20170122_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendeeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default='', max_length=1000)),
                ('rsvp_email_sent', models.BooleanField(default=False)),
                ('rsvp_confirmed', models.BooleanField(default=False)),
                ('checked_in', models.BooleanField(default=False)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hackathon')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='hackerinfo',
            name='checked_in',
        ),
        migrations.RemoveField(
            model_name='hackerinfo',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='hackerinfo',
            name='misc_info',
        ),
        migrations.RemoveField(
            model_name='hackerinfo',
            name='rsvp',
        ),
        migrations.RemoveField(
            model_name='judgeinfo',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='judgeinfo',
            name='misc_info',
        ),
        migrations.RemoveField(
            model_name='mentorinfo',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='mentorinfo',
            name='misc_info',
        ),
        migrations.RemoveField(
            model_name='organizerinfo',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='organizerinfo',
            name='misc_info',
        ),
        migrations.AddField(
            model_name='judgeinfo',
            name='organizer_contact',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='availability',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='motivation',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='skills',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizerinfo',
            name='motivation',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizerinfo',
            name='teams',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hackerinfo',
            name='attendee_status',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.AttendeeStatus'),
        ),
        migrations.AddField(
            model_name='judgeinfo',
            name='attendee_status',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.AttendeeStatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='attendee_status',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.AttendeeStatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizerinfo',
            name='attendee_status',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.AttendeeStatus'),
            preserve_default=False,
        ),
    ]
