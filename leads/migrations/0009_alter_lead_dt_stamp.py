# Generated by Django 4.0.5 on 2022-09-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_lead_dt_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='dt_stamp',
            field=models.DateTimeField(auto_created=True, auto_now=True, null=True),
        ),
    ]