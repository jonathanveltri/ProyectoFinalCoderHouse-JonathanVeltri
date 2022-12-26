# Generated by Django 4.1.2 on 2022-10-31 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('federation', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('fundation_date', models.DateField()),
            ],
        ),
    ]