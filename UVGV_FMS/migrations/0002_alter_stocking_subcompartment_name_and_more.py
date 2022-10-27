# Generated by Django 4.1 on 2022-10-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UVGV_FMS", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stocking",
            name="SubCompartment_Name",
            field=models.ForeignKey(
                default="15B1S1",
                on_delete=django.db.models.deletion.CASCADE,
                to="UVGV_FMS.subcompartmentregister",
                verbose_name="Block Name",
            ),
        ),
        migrations.AlterField(
            model_name="subcompartmentregister",
            name="Planting_Year",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="UVGV_FMS.plantingseason",
                verbose_name="Planting Season",
            ),
        ),
        migrations.AlterField(
            model_name="subcompartmentregister",
            name="Project_Name",
            field=models.ForeignKey(
                default="I",
                on_delete=django.db.models.deletion.CASCADE,
                to="UVGV_FMS.project",
                verbose_name="Project Name",
            ),
        ),
        migrations.AlterField(
            model_name="subcompartmentregister",
            name="SubCompartment_Name",
            field=models.CharField(
                max_length=10,
                primary_key=True,
                serialize=False,
                verbose_name="Block Name ",
            ),
        ),
    ]