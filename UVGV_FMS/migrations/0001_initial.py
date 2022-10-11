# Generated by Django 4.1 on 2022-10-08 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Espacement",
            fields=[
                (
                    "Espacement",
                    models.CharField(max_length=150, primary_key=True, serialize=False),
                ),
                ("RowSpacing", models.IntegerField()),
                ("InterRowSpacing", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PlantingSeason",
            fields=[
                (
                    "Planting_Season",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "Project_Name",
                    models.CharField(
                        choices=[("LLTC", "LLTC"), ("IT", "IT"), ("UVGV", "UVGV")],
                        default="I",
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Specie",
            fields=[
                (
                    "Specie",
                    models.CharField(max_length=150, primary_key=True, serialize=False),
                ),
                ("Vernacular_Name", models.CharField(max_length=150)),
                ("Standard_Form_Factor", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="WorkingCircle",
            fields=[
                (
                    "Usage",
                    models.CharField(
                        default="Fuelwood",
                        max_length=150,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubCompartmentRegister",
            fields=[
                (
                    "SubCompartment_Name",
                    models.CharField(
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        verbose_name="SubCompartment_Name ",
                    ),
                ),
                ("Compartment_Name", models.CharField(max_length=10)),
                ("Hectares", models.FloatField()),
                (
                    "Espacement",
                    models.ForeignKey(
                        default="3 x 2",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UVGV_FMS.espacement",
                        verbose_name="Espacement",
                    ),
                ),
                (
                    "Planting_Year",
                    models.ForeignKey(
                        default="2014/2015",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UVGV_FMS.plantingseason",
                        verbose_name="Planting_Season",
                    ),
                ),
                (
                    "Project_Name",
                    models.ForeignKey(
                        default="I",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UVGV_FMS.project",
                        verbose_name="Project_Name",
                    ),
                ),
                (
                    "Specie",
                    models.ForeignKey(
                        default="Eucalyptus tereticornis",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UVGV_FMS.specie",
                        verbose_name="Specie",
                    ),
                ),
                (
                    "WorkingCircles",
                    models.ForeignKey(
                        default="Fuelwood",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UVGV_FMS.workingcircle",
                        verbose_name="Usage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stocking",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Date", models.DateField(auto_now_add=True)),
                ("Surviving", models.IntegerField(null=True)),
                ("Dead", models.IntegerField()),
                (
                    "SubCompartment_Name",
                    models.ForeignKey(
                        default="15B1S1",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UVGV_FMS.subcompartmentregister",
                        verbose_name="SubCompartment_Name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StockingReport",
            fields=[],
            options={"proxy": True, "indexes": [], "constraints": [],},
            bases=("UVGV_FMS.subcompartmentregister",),
        ),
    ]