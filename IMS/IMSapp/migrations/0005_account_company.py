# Generated by Django 3.2.9 on 2021-11-18 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMSapp', '0004_auto_20211118_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMSapp.company'),
        ),
    ]
