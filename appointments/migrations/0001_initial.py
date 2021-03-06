# Generated by Django 3.0.5 on 2020-06-05 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('centers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('speciality', models.CharField(max_length=200)),
                ('center', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='cen_i_work_at', to='centers.Center')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_field', models.TimeField(blank=True, null=True)),
                ('date_field', models.DateField(blank=True, null=True)),
                ('doctor', models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.CASCADE, related_name='doc_name', to='appointments.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
