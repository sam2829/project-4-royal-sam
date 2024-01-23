# Generated by Django 3.2.22 on 2024-01-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('07:30', '07:30'), ('07:50', '07:50'), ('08:10', '08:10'), ('08:30', '08:30'), ('08:50', '08:50'), ('09:10', '09:10'), ('09:30', '09:30'), ('09:50', '09:50'), ('10:10', '10:10'), ('10:30', '10:30'), ('10:50', '10:50'), ('11:10', '11:10'), ('11:30', '11:30'), ('11:50', '11:50'), ('12:10', '12:10'), ('12:30', '12:30'), ('12:50', '12:50'), ('13:10', '13:10'), ('13:30', '13:30'), ('13:50', '13:50'), ('14:10', '14:10'), ('14:30', '14:30'), ('14:50', '14:50'), ('15:10', '15:10'), ('15:30', '15:30'), ('15:50', '15:50'), ('16:10', '16:10'), ('16:30', '16:30'), ('16:50', '16:50'), ('17:10', '17:10'), ('17:30', '17:30'), ('17:50', '17:50')], default='07:30', max_length=10),
        ),
    ]
