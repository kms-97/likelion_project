# Generated by Django 3.2.3 on 2021-05-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20210523_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='pay',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='period',
            field=models.IntegerField(null=True),
        ),
    ]
