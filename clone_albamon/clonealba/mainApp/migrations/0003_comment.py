# Generated by Django 3.2.3 on 2021-05-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20210520_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writter', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('notice_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.notice')),
            ],
        ),
    ]
