# Generated by Django 4.1 on 2022-10-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UVGV_FMS", "0005_alter_flutteruser_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flutteruser",
            name="Password",
            field=models.CharField(max_length=50),
        ),
    ]
