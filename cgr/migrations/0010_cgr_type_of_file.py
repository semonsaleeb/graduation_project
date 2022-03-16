# Generated by Django 4.0.2 on 2022-03-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgr', '0009_remove_cgr_is_fasta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cgr',
            name='type_of_file',
            field=models.CharField(choices=[('A', 'FASTA'), ('Q', 'FASTAQ')], default='FASTA', max_length=2),
        ),
    ]