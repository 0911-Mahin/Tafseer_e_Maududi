# Generated by Django 4.0.4 on 2022-04-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hizb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hizb_number', models.IntegerField()),
                ('verse_count', models.IntegerField()),
            ],
        ),
    ]
