# Generated by Django 4.1 on 2022-10-27 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UVGV_FMS", "0006_alter_flutteruser_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="stocking",
            name="UserName",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="UVGV_FMS.flutteruser",
                verbose_name="Data Collector",
            ),
        ),
    ]
