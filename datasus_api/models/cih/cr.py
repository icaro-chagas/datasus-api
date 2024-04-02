from django.db import models

class CRCih(models.Model):
    ano_cmpt = models.CharField(max_length=10, db_index=True)
    mes_cmpt = models.CharField(max_length=15, db_index=True)
    espec = models.CharField(max_length=20, db_index=True)
    cgc_hosp = models.CharField(max_length=20, db_index=True)
    munic_res = models.CharField(max_length=20, db_index=True)
    nasc = models.CharField(max_length=10, db_index=True)
    sexo = models.CharField(max_length=10, db_index=True)
    uti_mes_to = models.CharField(max_length=20, db_index=True)
    uti_int_to = models.CharField(max_length=20, db_index=True)
    proc_rea = models.CharField(max_length=20, db_index=True)
    dt_inter = models.CharField(max_length=20, db_index=True)
    dt_saida = models.CharField(max_length=20, db_index=True)
    diag_princ = models.CharField(max_length=20, db_index=True)
    diag_secun = models.CharField(max_length=20, db_index=True)
    cobranca = models.CharField(max_length=20, db_index=True)
    natureza = models.CharField(max_length=20, db_index=True)
    gestao = models.CharField(max_length=20, db_index=True)
    munic_mov = models.CharField(max_length=20, db_index=True)
    cod_idade = models.CharField(max_length=20, db_index=True)
    idade = models.IntegerField(null=True)
    dias_perm = models.CharField(max_length=20, db_index=True)
    morte = models.CharField(max_length=20, db_index=True)
    nacional = models.CharField(max_length=20, db_index=True)
    car_int = models.CharField(max_length=20, db_index=True)
    homonimo = models.CharField(max_length=20, db_index=True)
    cnes = models.CharField(max_length=20, db_index=True)
    fonte =  models.CharField(max_length=20, db_index=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'cr_cih'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]