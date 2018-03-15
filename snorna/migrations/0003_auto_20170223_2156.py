# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorna', '0002_clinical_genomic_analysis_snorna_expression'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='read_length',
            new_name='average_mappable_reads',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='sequencing_strategy',
        ),
        migrations.AddField(
            model_name='dataset',
            name='snorna_n',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='snorna_rpkm_n',
            field=models.IntegerField(null=True),
        ),
    ]
