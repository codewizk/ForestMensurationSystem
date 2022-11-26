# Generated by Django 3.2 on 2022-10-31 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UVGV_FMS', '0007_stocking_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SampleNo', models.CharField(max_length=150)),
                ('TreeNo', models.IntegerField()),
                ('DBH', models.IntegerField()),
                ('Height', models.FloatField()),
                ('SubCompartment_Name', models.ForeignKey(default='15B1S1', on_delete=django.db.models.deletion.CASCADE, to='UVGV_FMS.subcompartmentregister', verbose_name='Block Name')),
            ],
        ),
    ]
