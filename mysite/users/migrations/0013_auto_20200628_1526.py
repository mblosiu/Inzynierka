# Generated by Django 3.0.7 on 2020-06-28 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_account_race_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='matching_form',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.MatchingForm'),
        ),
    ]
