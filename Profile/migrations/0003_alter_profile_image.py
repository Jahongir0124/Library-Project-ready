# Generated by Django 4.1.1 on 2022-10-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_profile_image_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='media/photoUsers'),
            preserve_default=False,
        ),
    ]
