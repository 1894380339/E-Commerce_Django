# Generated by Django 3.2 on 2022-05-19 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_auto_20220518_0927"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prod_gallery",
                to="app.product",
            ),
        ),
    ]
