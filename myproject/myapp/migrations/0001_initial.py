# Generated by Django 5.1.6 on 2025-02-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('support_fund', models.IntegerField()),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
    ]
