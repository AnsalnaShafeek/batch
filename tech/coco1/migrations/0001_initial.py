# Generated by Django 4.1.3 on 2022-12-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('passwd', models.CharField(max_length=25)),
                ('cpasswd', models.CharField(max_length=25)),
            ],
        ),
    ]
