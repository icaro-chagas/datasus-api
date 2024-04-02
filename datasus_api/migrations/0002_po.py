# Generated by Django 4.2.10 on 2024-03-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasus_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_diagn', models.CharField(max_length=20, null=True)),
                ('anomes_dia', models.CharField(max_length=20, null=True)),
                ('ano_tratam', models.CharField(max_length=20, null=True)),
                ('anomes_tra', models.CharField(max_length=20, null=True)),
                ('uf_resid', models.CharField(max_length=20, null=True)),
                ('mun_resid', models.CharField(max_length=20, null=True)),
                ('uf_tratam', models.CharField(max_length=20, null=True)),
                ('mun_tratam', models.CharField(max_length=20, null=True)),
                ('uf_diagn', models.CharField(max_length=20, null=True)),
                ('mun_diag', models.CharField(max_length=20, null=True)),
                ('tratamento', models.CharField(max_length=20, null=True)),
                ('diagnostic', models.CharField(max_length=20, null=True)),
                ('idade', models.CharField(max_length=20, null=True)),
                ('sexo', models.CharField(max_length=20, null=True)),
                ('estadiam', models.CharField(max_length=20, null=True)),
                ('cnes_diag', models.CharField(max_length=20, null=True)),
                ('cnes_trat', models.CharField(max_length=20, null=True)),
                ('tempo_trat', models.CharField(max_length=20, null=True)),
                ('cns_pac', models.CharField(max_length=20, null=True)),
                ('diag_deth', models.CharField(max_length=20, null=True)),
                ('dt_diag', models.CharField(max_length=20, null=True)),
                ('dt_trat', models.CharField(max_length=20, null=True)),
                ('dt_nasc', models.CharField(max_length=20, null=True)),
                ('uf', models.CharField(db_index=True, max_length=3)),
                ('ano', models.CharField(db_index=True, max_length=4)),
            ],
            options={
                'db_table': 'po',
                'indexes': [models.Index(fields=['uf', 'ano'], name='po_uf_0d7bdd_idx')],
            },
        ),
    ]
