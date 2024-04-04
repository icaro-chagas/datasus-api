# Generated by Django 4.2.10 on 2024-04-04 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasus_api', '0004_absiasus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absiasus',
            name='ab_anoacom',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_dtcirg2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_dtcirur',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_imc',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_mesacom',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_numaih',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_numaih2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_pontbar',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_prcaih2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_prcaih3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_procaih',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ab_tabbarr',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_alta',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_apacant',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_autoriz',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_catend',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_ceppcn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cidcas',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cidpri',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cidsec',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cmp',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cnpjcpf',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cnpjmnt',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_cnspcn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_codemi',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_coduni',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_coidade',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_condic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_dtaut',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_dtfim',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_dtinic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_dtocor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_dtsolic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_encerr',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_etnia',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_gestao',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_mn_ind',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_mndif',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_motsai',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_munpcn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_mvm',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_natjur',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_nuidade',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_obito',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_perman',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_pripal',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_racacor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_sexo',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_tippre',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_tpapac',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_tpaten',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_tpups',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_transf',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_ufdif',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_ufmun',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_ufnacio',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='absiasus',
            name='ap_unisol',
            field=models.CharField(max_length=20, null=True),
        ),
    ]