# Generated by Django 3.0.8 on 2020-07-25 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200725_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('hair_color_blonde_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('hair_color_brunette_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('hair_color_red_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('growth_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('weight_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('body_type_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('freckles_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('glasses_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('hair_length_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('is_smoking_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('is_drinking_alcohol_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Assertiveness_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Sincerity_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Empathy_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Communication_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Selflessness_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Honesty_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Scrupulousness_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Diligence_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('Kindness_preference', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dark_theme', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Assertiveness_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Communication_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Diligence_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Empathy_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Honesty_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Kindness_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Scrupulousness_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Selflessness_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Sincerity_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='body_type_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='freckles_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='glasses_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='growth_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hair_color_blonde_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hair_color_brunette_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hair_color_red_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hair_length_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_drinking_alcohol_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_smoking_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='matching_form',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex_preference',
        ),
        migrations.RemoveField(
            model_name='user',
            name='weight_preference',
        ),
        migrations.DeleteModel(
            name='MatchingForm',
        ),
        migrations.AddField(
            model_name='user',
            name='preferences',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Preferences'),
        ),
        migrations.AddField(
            model_name='user',
            name='settings',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Settings'),
        ),
    ]
