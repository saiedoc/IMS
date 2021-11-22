# Generated by Django 3.2.9 on 2021-11-22 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductsAndCompanies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductsAndCompanies.company')),
            ],
        ),
    ]