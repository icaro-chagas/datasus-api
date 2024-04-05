from django.db import models

class SPSihsus(models.Model):
    sp_gestor = models.CharField(max_length=65, null=True)
    sp_uf = models.CharField(max_length=65, null=True)
    sp_aa = models.CharField(max_length=65, null=True)
    sp_mm = models.CharField(max_length=65, null=True)
    sp_cnes = models.CharField(max_length=65, null=True)
    sp_naih = models.CharField(max_length=65, null=True)
    sp_procrea = models.CharField(max_length=65, null=True)
    sp_dtinter = models.CharField(max_length=65, null=True)
    sp_dtsaida = models.CharField(max_length=65, null=True)
    sp_num_pr = models.CharField(max_length=65, null=True)
    sp_tipo = models.CharField(max_length=65, null=True)
    sp_cpfcgc = models.CharField(max_length=65, null=True)
    sp_atoprof = models.CharField(max_length=65, null=True)
    sp_tp_ato = models.CharField(max_length=65, null=True)
    sp_qtd_ato = models.IntegerField(null=True)
    sp_ptsp = models.CharField(max_length=65, null=True)
    sp_nf = models.CharField(max_length=65, null=True)
    sp_valato = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    sp_m_hosp = models.CharField(max_length=65, null=True)
    sp_m_pac = models.CharField(max_length=65, null=True)
    sp_des_hos = models.CharField(max_length=65, null=True)
    sp_des_pac = models.CharField(max_length=65, null=True)
    sp_complex = models.CharField(max_length=65, null=True)
    sp_financ = models.CharField(max_length=65, null=True)
    sp_co_faec = models.CharField(max_length=65, null=True)
    sp_pf_cbo = models.CharField(max_length=65, null=True)
    sp_pf_doc = models.CharField(max_length=65, null=True)
    sp_pj_doc = models.CharField(max_length=65, null=True)
    in_tp_val = models.CharField(max_length=65, null=True)
    sequencia = models.CharField(max_length=65, null=True)
    remessa = models.CharField(max_length=65, null=True)
    serv_cla = models.CharField(max_length=65, null=True)
    sp_cidpri = models.CharField(max_length=65, null=True)
    sp_cidsec = models.CharField(max_length=65, null=True)
    sp_qt_proc = models.IntegerField(null=True)
    sp_u_aih = models.CharField(max_length=65, null=True)
    remessa = models.CharField(max_length=65, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)


    class Meta:
        db_table = 'sp_sihsus'

        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]