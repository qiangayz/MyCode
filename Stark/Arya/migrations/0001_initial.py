# Generated by Django 2.0.5 on 2018-05-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32)),
                ('key', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Waiting'), (1, 'Accepted'), (2, 'Rejected')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('host', models.ManyToManyField(blank=True, to='Arya.Host')),
            ],
        ),
    ]
