# Generated by Django 3.0.4 on 2020-04-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('email_id', models.CharField(max_length=23)),
                ('password', models.CharField(max_length=23)),
                ('age', models.CharField(max_length=23)),
            ],
        ),
    ]
