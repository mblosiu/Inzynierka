# Generated by Django 3.1 on 2020-08-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200812_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='body_type',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]