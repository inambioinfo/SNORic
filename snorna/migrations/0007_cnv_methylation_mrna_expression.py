# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorna', '0006_snorna_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='cnv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snorna', models.CharField(max_length=225, null=True)),
                ('dataset_id', models.CharField(max_length=225, null=True)),
                ('sample_id', models.CharField(max_length=225, null=True)),
                ('copy', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='methylation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snorna', models.CharField(max_length=225, null=True)),
                ('dataset_id', models.CharField(max_length=225, null=True)),
                ('sample_id', models.CharField(max_length=225, null=True)),
                ('chrom', models.CharField(max_length=10, null=True)),
                ('strand', models.CharField(max_length=4, null=True)),
                ('start', models.IntegerField(null=True)),
                ('end', models.IntegerField(null=True)),
                ('source', models.CharField(max_length=45, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('meth_id', models.CharField(max_length=225, null=True)),
                ('pos', models.IntegerField(null=True)),
                ('level', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mrna_expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snorna', models.CharField(max_length=225, null=True)),
                ('dataset_id', models.CharField(max_length=225, null=True)),
                ('gene_symbol', models.CharField(max_length=225, null=True)),
                ('host', models.IntegerField(null=True)),
                ('spearman_corr', models.FloatField(null=True)),
                ('p_value', models.FloatField(null=True)),
                ('fdr', models.FloatField(null=True)),
                ('sample_id', models.CharField(max_length=225, null=True)),
                ('rna_expression', models.FloatField(null=True)),
            ],
        ),
    ]
