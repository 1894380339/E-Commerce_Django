# Generated by Django 3.2 on 2022-05-18 02:12

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_gallery_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img_product",
            field=models.FileField(
                blank=True,
                storage=gdstorage.storage.GoogleDriveStorage(),
                upload_to="maps/",
            ),
        ),
    ]
