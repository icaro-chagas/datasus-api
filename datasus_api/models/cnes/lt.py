from django.db import models

class LTCnes(models.Model):
    cnes = models.CharField(max_length=20, null=True)
    codufmun = models.CharField(max_length=20, null=True)
    regsaude = models.CharField(max_length=20, null=True)
    micr_reg = models.CharField(max_length=20, null=True)
    distrsan = models.CharField(max_length=20, null=True)
    distradm = models.CharField(max_length=20, null=True)
    tpgestao = models.CharField(max_length=20, null=True)
    pf_pj = models.CharField(max_length=20, null=True)
    cpf_cnpj = models.CharField(max_length=20, null=True)
    niv_dep = models.CharField(max_length=20, null=True)
    cnpj_man = models.CharField(max_length=20, null=True)
    esfera_a = models.CharField(max_length=20, null=True)
    atividad = models.CharField(max_length=20, null=True)
    retencao = models.CharField(max_length=20, null=True)
    natureza = models.CharField(max_length=20, null=True)
    clientel = models.CharField(max_length=20, null=True)
    tp_unid = models.CharField(max_length=20, null=True)
    turno_at = models.CharField(max_length=20, null=True)
    niv_hier = models.CharField(max_length=20, null=True)
    terceiro = models.CharField(max_length=20, null=True)
    tp_leito = models.CharField(max_length=20, null=True)
    codleito = models.CharField(max_length=20, null=True)
    qt_exist = models.IntegerField(null=True)
    qt_contr = models.IntegerField(null=True)
    qt_sus = models.IntegerField(null=True)
    qt_nsus = models.IntegerField(null=True)
    competen = models.CharField(max_length=20, null=True)
    nat_jur = models.CharField(max_length=20, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'lt_cnes'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]