from django.db import models

class ERSihsus(models.Model):
    sequencia = models.CharField(max_length=25, null=True)
    remessa = models.CharField(max_length=25, null=True)
    cnes = models.CharField(max_length=25, null=True)
    aih = models.CharField(max_length=25, null=True)
    ano = models.CharField(max_length=25, null=True)
    mes = models.CharField(max_length=25, null=True)
    dt_inter = models.CharField(max_length=25, null=True)
    dt_saida = models.CharField(max_length=25, null=True)
    mun_mov = models.CharField(max_length=25, null=True)
    uf_zi = models.CharField(max_length=25, null=True)
    mun_res = models.CharField(max_length=25, null=True)
    uf_res = models.CharField(max_length=25, null=True)
    co_erro = models.CharField(max_length=25, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)


    class Meta:
        db_table = 'er_sihsus'

        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]