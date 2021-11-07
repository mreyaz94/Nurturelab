# Generated by Django 3.1.4 on 2021-10-27 07:45

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
            name='Advisors_DB',
            fields=[
                ('adv_name', models.CharField(max_length=40)),
                ('adv_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('adv_pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_DB',
            fields=[
                ('booking_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('booking_time', models.DateTimeField(auto_now=True)),
                ('schedule_time', models.DateTimeField()),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.advisors_db')),
                ('booked_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]