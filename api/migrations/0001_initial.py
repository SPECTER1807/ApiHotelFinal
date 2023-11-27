# Generated by Django 3.2.4 on 2023-11-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postalcode', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(max_length=255)),
                ('arrive', models.DateField()),
                ('depart', models.DateField()),
                ('amtpple', models.IntegerField()),
                ('amtrms', models.IntegerField()),
                ('rmtype', models.CharField(max_length=255)),
                ('comments', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
