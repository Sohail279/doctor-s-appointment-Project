# Generated by Django 4.1 on 2022-11-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_nearby_doctor_clinicloc'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearby_doctor',
            name='nw_pat_fee',
            field=models.CharField(default=' ', max_length=122),
            preserve_default=False,
        ),
    ]