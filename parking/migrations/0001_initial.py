# Generated by Django 3.2 on 2022-03-23 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('doors', models.IntegerField(default=2)),
                ('capacity_engine', models.IntegerField()),
                ('date_fabricanted', models.DateField()),
                ('mechanical_revision', models.BooleanField(default=True)),
                ('plate', models.CharField(max_length=6)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.car')),
            ],
        ),
    ]