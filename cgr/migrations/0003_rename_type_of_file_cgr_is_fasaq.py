# Generated by Django 4.0.2 on 2022-03-13 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cgr', '0002_img_cgr_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cgr',
            old_name='type_of_file',
            new_name='is_FASAQ',
        ),
    ]
