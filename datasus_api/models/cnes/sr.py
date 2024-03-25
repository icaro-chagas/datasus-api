from django.db import models

class SRCnes(models.Model):
    cnes = models.CharField(max_length=60, null=True)
    codufmun = models.CharField(max_length=60, null=True)
    serv_esp = models.CharField(max_length=60, null=True)
    class_sr = models.CharField(max_length=60, null=True)
    srvunico = models.CharField(max_length=60, null=True)
    regsaude = models.CharField(max_length=60, null=True)
    micr_reg = models.CharField(max_length=60, null=True)
    distrsan = models.CharField(max_length=60, null=True)
    distradm = models.CharField(max_length=60, null=True)
    tpgestao = models.CharField(max_length=60, null=True)
    pf_pj = models.CharField(max_length=60, null=True)
    cpf_cnpj = models.CharField(max_length=160, null=True)
    niv_dep = models.CharField(max_length=60, null=True)
    esfera_a = models.CharField(max_length=60, null=True)
    atividad = models.CharField(max_length=60, null=True)
    retencao = models.CharField(max_length=60, null=True)
    natureza = models.CharField(max_length=60, null=True)
    clientel = models.CharField(max_length=60, null=True)
    tp_unid = models.CharField(max_length=60, null=True)
    turno_at = models.CharField(max_length=60, null=True)
    niv_hier = models.CharField(max_length=60, null=True)
    terceiro = models.CharField(max_length=60, null=True)
    cnpj_man = models.CharField(max_length=160, null=True)
    caracter = models.CharField(max_length=60, null=True)
    amb_nsus = models.CharField(max_length=60, null=True)
    amb_sus = models.CharField(max_length=60, null=True)
    hosp_nsus = models.CharField(max_length=60, null=True)
    hosp_sus = models.CharField(max_length=60, null=True)
    competen = models.CharField(max_length=60, null=True)
    contsrvu = models.CharField(max_length=60, null=True)
    cnesterc = models.CharField(max_length=60, null=True)
    nat_jur = models.CharField(max_length=60, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'sr_cnes'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]