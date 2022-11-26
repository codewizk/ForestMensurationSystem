# Generated by Django 3.2 on 2022-11-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UVGV_FMS', '0009_volume_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagepath', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('predicted', models.TextField()),
                ('confidence', models.IntegerField(blank=True, default=0, null=True)),
                ('saved', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-saved',),
            },
        ),
        migrations.AlterModelOptions(
            name='stockingreport',
            options={'verbose_name': 'Stocking Summary Report', 'verbose_name_plural': 'Stocking Summary Report'},
        ),
        migrations.AlterModelOptions(
            name='subcompartmentregister',
            options={'verbose_name': 'Compartment Register', 'verbose_name_plural': 'Compartments Register'},
        ),
        migrations.AlterField(
            model_name='volume',
            name='Height',
            field=models.DecimalField(decimal_places=1, max_digits=9, verbose_name='Height'),
        ),
    ]
