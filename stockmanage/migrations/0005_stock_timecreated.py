# Generated by Django 3.0.8 on 2020-07-25 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanage', '0004_auto_20200726_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='timeCreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]