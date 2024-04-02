from django.db import models

class CIHA(models.Model):
    ano_cmpt = models.CharField(max_length=25, null=True)
    mes_cmpt = models.CharField(max_length=25, null=True)
    espec = models.CharField(max_length=25, null=True)
    cgc_hosp = models.CharField(max_length=25, null=True)
    munic_res = models.CharField(max_length=25, null=True)
    nasc = models.CharField(max_length=25, null=True)
    sexo = models.CharField(max_length=25, null=True)
    uti_mes_to = models.CharField(max_length=25, null=True)
    uti_int_to = models.CharField(max_length=25, null=True)
    proc_rea = models.CharField(max_length=25, null=True)
    qt_proc = models.CharField(max_length=25, null=True)
    dt_atend = models.CharField(max_length=25, null=True)
    dt_saida = models.CharField(max_length=25, null=True)
    diag_princ = models.CharField(max_length=25, null=True)
    diag_secun = models.CharField(max_length=25, null=True)
    cobranca = models.CharField(max_length=25, null=True)
    natureza = models.CharField(max_length=25, null=True)
    gestao = models.CharField(max_length=25, null=True)
    munic_mov = models.CharField(max_length=25, null=True)
    cod_idade = models.CharField(max_length=25, null=True)
    idade = models.CharField(max_length=25, null=True)
    dias_perm = models.CharField(max_length=25, null=True)
    morte = models.CharField(max_length=25, null=True)
    nacional = models.CharField(max_length=25, null=True)
    car_int = models.CharField(max_length=25, null=True)
    homonimo = models.CharField(max_length=25, null=True)
    cnes = models.CharField(max_length=25, null=True)
    fonte = models.CharField(max_length=25, null=True)
    modalidade = models.CharField(max_length=25, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'ciha'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]