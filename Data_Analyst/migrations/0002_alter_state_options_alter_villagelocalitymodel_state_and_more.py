# Generated by Django 4.2.6 on 2023-11-26 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Data_Analyst", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="state",
            options={"ordering": ["state"]},
        ),
        migrations.AlterField(
            model_name="villagelocalitymodel",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Data_Analyst.state",
                verbose_name="State",
            ),
        ),
        migrations.RemoveField(
            model_name="villagelocalitymodel",
            name="village",
        ),
        migrations.AddField(
            model_name="villagelocalitymodel",
            name="village",
            field=models.ManyToManyField(
                to="Data_Analyst.villagemappingfile", verbose_name="Excel File"
            ),
        ),
    ]