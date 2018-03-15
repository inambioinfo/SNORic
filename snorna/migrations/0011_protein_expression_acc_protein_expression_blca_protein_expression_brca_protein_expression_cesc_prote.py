# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snorna', '0010_protein_expression'),
    ]

    operations = [
        migrations.CreateModel(
            name='protein_expression_ACC',
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
        migrations.CreateModel(
            name='protein_expression_BLCA',
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
        migrations.CreateModel(
            name='protein_expression_BRCA',
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
        migrations.CreateModel(
            name='protein_expression_CESC',
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
        migrations.CreateModel(
            name='protein_expression_CHOL',
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
        migrations.CreateModel(
            name='protein_expression_COAD',
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
        migrations.CreateModel(
            name='protein_expression_DLBC',
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
        migrations.CreateModel(
            name='protein_expression_ESCA',
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
        migrations.CreateModel(
            name='protein_expression_HNSC',
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
        migrations.CreateModel(
            name='protein_expression_KICH',
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
        migrations.CreateModel(
            name='protein_expression_KIRC',
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
        migrations.CreateModel(
            name='protein_expression_KIRP',
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
        migrations.CreateModel(
            name='protein_expression_LGG',
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
        migrations.CreateModel(
            name='protein_expression_LIHC',
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
        migrations.CreateModel(
            name='protein_expression_LUAD',
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
        migrations.CreateModel(
            name='protein_expression_LUSC',
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
        migrations.CreateModel(
            name='protein_expression_MESO',
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
        migrations.CreateModel(
            name='protein_expression_OV',
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
        migrations.CreateModel(
            name='protein_expression_PAAD',
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
        migrations.CreateModel(
            name='protein_expression_PCPG',
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
        migrations.CreateModel(
            name='protein_expression_PRAD',
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
        migrations.CreateModel(
            name='protein_expression_READ',
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
        migrations.CreateModel(
            name='protein_expression_SARC',
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
        migrations.CreateModel(
            name='protein_expression_SKCM',
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
        migrations.CreateModel(
            name='protein_expression_STAD',
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
        migrations.CreateModel(
            name='protein_expression_TGCT',
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
        migrations.CreateModel(
            name='protein_expression_THCA',
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
        migrations.CreateModel(
            name='protein_expression_THYM',
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
        migrations.CreateModel(
            name='protein_expression_UCEC',
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
        migrations.CreateModel(
            name='protein_expression_UCS',
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
        migrations.CreateModel(
            name='protein_expression_UVM',
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