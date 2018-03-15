# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorna', '0009_cnv_acc_cnv_blca_cnv_brca_cnv_cesc_cnv_chol_cnv_coad_cnv_dlbc_cnv_esca_cnv_hnsc_cnv_kich_cnv_kirc_cn'),
    ]

    operations = [
        migrations.CreateModel(
            name='protein_expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snorna', models.CharField(max_length=225, null=True)),
                ('dataset_id', models.CharField(max_length=225, null=True)),
                ('protein', models.CharField(max_length=225, null=True)),
                ('spearman_corr', models.FloatField(null=True)),
                ('p_value', models.FloatField(null=True)),
                ('fdr', models.FloatField(null=True)),
                ('sample_id', models.CharField(max_length=225, null=True)),
                ('rna_expression', models.FloatField(null=True)),
            ],
        ),
    ]
