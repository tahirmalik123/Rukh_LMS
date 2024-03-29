# Generated by Django 4.0.2 on 2022-02-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_addbooks_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
