# Generated by Django 4.1.7 on 2023-03-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DRF_App', '0002_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
