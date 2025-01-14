# Generated by Django 5.1.4 on 2025-01-14 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volonteer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='total_hours',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='event',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='coordinator',
            field=models.ForeignKey(limit_choices_to={'role': 'coordinator'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinator_events', to='volonteer.user'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registered_volunteers',
            field=models.ManyToManyField(blank=True, related_name='registered_events', to='volonteer.user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_volunteers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'volunteer'}, related_name='tasks', to='volonteer.user'),
        ),
    ]
