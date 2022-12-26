# Generated by Django 4.1.2 on 2022-11-27 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('federations', '0003_alter_federation_image'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='federation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='federations.federation'),
        ),
    ]