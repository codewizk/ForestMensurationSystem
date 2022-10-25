# Generated by Django 4.1 on 2022-10-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UVGV_FMS", "0002_alter_stocking_subcompartment_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FlutterUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("UserName", models.CharField(max_length=150)),
                ("Email", models.EmailField(max_length=250)),
                ("Password", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "FlutterUser",
                "verbose_name_plural": "FlutterUsers",
            },
        ),
    ]
