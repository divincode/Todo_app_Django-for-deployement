# Generated by Django 3.1.6 on 2021-03-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskTitle', models.CharField(max_length=30)),
                ('TaskDesc', models.TextField(max_length=1000)),
            ],
        ),
    ]
