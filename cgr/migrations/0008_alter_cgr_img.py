# Generated by Django 4.0.2 on 2022-03-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgr', '0007_alter_cgr_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cgr',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='documents/'),
        ),
    ]
