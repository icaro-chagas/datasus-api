from django.db import models

class PNSisprenatal(models.Model):
    nu_ano_ges = models.CharField(max_length=60, null=True)
    dt_atend = models.CharField(max_length=60, null=True)
    co_uf_ibge = models.CharField(max_length=60, null=True)
    nu_gesta = models.CharField(max_length=60, null=True)
    co_gestant = models.CharField(max_length=60, null=True)
    co_pais = models.CharField(max_length=60, null=True)
    nu_cns = models.CharField(max_length=60, null=True)
    nu_idade = models.CharField(max_length=60, null=True)
    nu_nis = models.CharField(max_length=60, null=True)
    nu_nis_rep = models.CharField(max_length=60, null=True)
    ds_zona = models.CharField(max_length=60, null=True)
    qt_ab_ect = models.CharField(max_length=60, null=True)
    qt_ab_ger = models.CharField(max_length=60, null=True)
    qt_ab_mol = models.CharField(max_length=60, null=True)
    qt_mor_aps = models.CharField(max_length=60, null=True)
    qt_mor_ps = models.CharField(max_length=60, null=True)
    qt_nsc_mor = models.CharField(max_length=60, null=True)
    qt_nsc_viv = models.CharField(max_length=60, null=True)
    qt_prt_cir = models.CharField(max_length=60, null=True)
    qt_prt_for = models.CharField(max_length=60, null=True)
    qt_prt_vag = models.CharField(max_length=60, null=True)
    st_aux_dsl = models.CharField(max_length=60, null=True)
    st_gra_ant = models.CharField(max_length=60, null=True)
    st_gra_pla = models.CharField(max_length=60, null=True)
    dt_dum = models.CharField(max_length=60, null=True)
    dt_dpp = models.CharField(max_length=60, null=True)
    co_tpo_gra = models.CharField(max_length=60, null=True)
    co_esc_gp = models.CharField(max_length=60, null=True)
    co_rac_gp = models.CharField(max_length=60, null=True)
    co_etn_gp = models.CharField(max_length=60, null=True)
    co_stf_gp = models.CharField(max_length=60, null=True)
    co_mun_ubs = models.CharField(max_length=60, null=True)
    qt_cons = models.CharField(max_length=60, null=True)
    qt_consult = models.CharField(max_length=60, null=True)
    st_gestac = models.CharField(max_length=60, null=True)
    dt_inc = models.CharField(max_length=60, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'pn_sisprenatal'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]