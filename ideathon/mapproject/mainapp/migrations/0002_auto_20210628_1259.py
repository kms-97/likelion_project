# Generated by Django 3.2.4 on 2021-06-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Addr', models.TextField()),
                ('Tele', models.TextField()),
                ('Mono', models.TextField(blank=True, null=True)),
                ('Monc', models.TextField(blank=True, null=True)),
                ('Tueo', models.TextField(blank=True, null=True)),
                ('Tuec', models.TextField(blank=True, null=True)),
                ('Wedo', models.TextField(blank=True, null=True)),
                ('Wedc', models.TextField(blank=True, null=True)),
                ('Thuo', models.TextField(blank=True, null=True)),
                ('Thuc', models.TextField(blank=True, null=True)),
                ('Frio', models.TextField(blank=True, null=True)),
                ('Fric', models.TextField(blank=True, null=True)),
                ('Sato', models.TextField(blank=True, null=True)),
                ('Satc', models.TextField(blank=True, null=True)),
                ('Suno', models.TextField(blank=True, null=True)),
                ('Sunc', models.TextField(blank=True, null=True)),
                ('Hpid', models.TextField()),
                ('Etc', models.TextField(blank=True, null=True)),
                ('Info', models.TextField(blank=True, null=True)),
                ('Map', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Teammate',
        ),
    ]