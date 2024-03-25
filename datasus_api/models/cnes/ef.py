from django.db import models

class EFCnes(models.Model):
    cnes = models.CharField(max_length=55, null=True)
    codufmun = models.CharField(max_length=55, null=True)
    regsaude = models.CharField(max_length=55, null=True)
    micr_reg = models.CharField(max_length=55, null=True)
    distrsan = models.CharField(max_length=55, null=True)
    distradm = models.CharField(max_length=55, null=True)
    tpgestao = models.CharField(max_length=55, null=True)
    pf_pj = models.CharField(max_length=55, null=True)
    cpf_cnpj = models.CharField(max_length=55, null=True)
    niv_dep = models.CharField(max_length=55, null=True)
    cnpj_man = models.CharField(max_length=55, null=True)
    esfera_a = models.CharField(max_length=55, null=True)
    retencao = models.CharField(max_length=55, null=True)
    atividad = models.CharField(max_length=55, null=True)
    natureza = models.CharField(max_length=55, null=True)
    clientel = models.CharField(max_length=55, null=True)
    tp_unid = models.CharField(max_length=55, null=True)
    turno_at = models.CharField(max_length=55, null=True)
    niv_hier = models.CharField(max_length=55, null=True)
    terceiro = models.CharField(max_length=55, null=True)
    cod_cep = models.CharField(max_length=55, null=True)
    vinc_sus = models.CharField(max_length=55, null=True)
    tp_prest = models.CharField(max_length=55, null=True)
    sgruphab = models.CharField(max_length=55, null=True)
    cmpt_ini = models.CharField(max_length=55, null=True)
    cmpt_fim = models.CharField(max_length=55, null=True)
    dtportar = models.CharField(max_length=55, null=True)
    portaria = models.CharField(max_length=55, null=True)
    maportar = models.CharField(max_length=55, null=True)
    competen = models.CharField(max_length=55, null=True)
    nat_jur = models.CharField(max_length=55, null=True)
    uf = models.CharField(max_length=5, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'ef_cnes'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]