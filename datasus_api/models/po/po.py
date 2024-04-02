from django.db import models

class PO(models.Model):
    ano_diagn = models.CharField(max_length=20, null=True)
    anomes_dia = models.CharField(max_length=20, null=True)
    ano_tratam = models.CharField(max_length=20, null=True)
    anomes_tra = models.CharField(max_length=20, null=True)
    uf_resid = models.CharField(max_length=20, null=True)
    mun_resid = models.CharField(max_length=20, null=True)
    uf_tratam = models.CharField(max_length=20, null=True)
    mun_tratam = models.CharField(max_length=20, null=True)
    uf_diagn = models.CharField(max_length=20, null=True)
    mun_diag = models.CharField(max_length=20, null=True)
    tratamento = models.CharField(max_length=20, null=True)
    diagnostic = models.CharField(max_length=20, null=True)
    idade = models.CharField(max_length=20, null=True)
    sexo = models.CharField(max_length=20, null=True)
    estadiam = models.CharField(max_length=20, null=True)
    cnes_diag = models.CharField(max_length=20, null=True)
    cnes_trat = models.CharField(max_length=20, null=True)
    tempo_trat = models.CharField(max_length=20, null=True)
    cns_pac = models.CharField(max_length=20, null=True)
    diag_deth = models.CharField(max_length=20, null=True)
    dt_diag = models.CharField(max_length=20, null=True)
    dt_trat = models.CharField(max_length=20, null=True)
    dt_nasc = models.CharField(max_length=20, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)

    class Meta:
        db_table = 'po'
        indexes = [
            models.Index(fields=['uf', 'ano'])
        ]