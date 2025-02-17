# Generated by Django 5.1.4 on 2025-01-11 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_volunteers', models.IntegerField(default=0)),
                ('total_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('male_volunteers', models.IntegerField(default=0)),
                ('female_volunteers', models.IntegerField(default=0)),
                ('other_gender_volunteers', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('role', models.CharField(choices=[('volunteer', 'Volunteer'), ('coordinator', 'Coordinator'), ('admin', 'Admin')], max_length=15)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('total_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('xp_points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('expired', 'Expired')], default='pending', max_length=15)),
                ('due_date', models.DateTimeField()),
                ('hours_to_complete', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_volunteers', models.ManyToManyField(limit_choices_to={'role': 'volunteer'}, related_name='tasks', to='volonteer.user')),
                ('coordinator', models.ForeignKey(limit_choices_to={'role': 'coordinator'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinator_tasks', to='volonteer.user')),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('xp_points', models.IntegerField(default=0)),
                ('total_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leaderboard', to='volonteer.user')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('total_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinator', models.ForeignKey(limit_choices_to={'role': 'coordinator'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='volonteer.user')),
                ('registered_volunteers', models.ManyToManyField(limit_choices_to={'role': 'volunteer'}, related_name='registered_events', to='volonteer.user')),
            ],
        ),
    ]
