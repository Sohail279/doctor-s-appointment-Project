# Generated by Django 4.1 on 2022-12-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_health'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='bllod_2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]