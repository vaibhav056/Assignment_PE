# Generated by Django 3.2.8 on 2022-07-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220701_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
