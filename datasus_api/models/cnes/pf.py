from django.db import models

class PFCnes(models.Model):
    cnes = models.CharField(max_length=65, null=True)
    codufmun = models.CharField(max_length=65, null=True)
    regsaude = models.CharField(max_length=65, null=True)
    micr_reg = models.CharField(max_length=65, null=True)
    distrsan = models.CharField(max_length=65, null=True)
    distradm = models.CharField(max_length=65, null=True)
    tpgestao = models.CharField(max_length=65, null=True)
    pf_pj = models.CharField(max_length=65, null=True)
    cpf_cnpj = models.CharField(max_length=65, null=True)
    niv_dep = models.CharField(max_length=65, null=True)
    cnpj_man = models.CharField(max_length=65, null=True)
    esfera_a = models.CharField(max_length=65, null=True)
    atividad = models.CharField(max_length=65, null=True)
    retencao = models.CharField(max_length=65, null=True)
    natureza = models.CharField(max_length=65, null=True)
    clientel = models.CharField(max_length=65, null=True)
    tp_unid = models.CharField(max_length=65, null=True)
    turno_at = models.CharField(max_length=65, null=True)
    niv_hier = models.CharField(max_length=65, null=True)
    terceiro = models.CharField(max_length=65, null=True)
    cpf_prof = models.CharField(max_length=65, null=True)
    cpfunico = models.CharField(max_length=65, null=True)
    cbo = models.CharField(max_length=65, null=True)
    cbounico = models.CharField(max_length=65, null=True)
    nomeprof = models.CharField(max_length=65, null=True)
    cns_prof = models.CharField(max_length=65, null=True)
    conselho = models.CharField(max_length=65, null=True)
    registro = models.CharField(max_length=65, null=True)
    vinculac = models.CharField(max_length=65, null=True)
    vincul_c = models.CharField(max_length=65, null=True)
    vincul_a = models.CharField(max_length=65, null=True)
    vincul_n = models.CharField(max_length=65, null=True)
    prof_sus = models.CharField(max_length=65, null=True)
    profnsus = models.CharField(max_length=65, null=True)
    horaoutr = models.CharField(max_length=65, null=True)
    horahosp = models.CharField(max_length=65, null=True)
    hora_amb = models.CharField(max_length=65, null=True)
    competen = models.CharField(max_length=65, null=True)
    ufmunres = models.CharField(max_length=65, null=True)
    nat_jur = models.CharField(max_length=65, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'pf_cnes'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]