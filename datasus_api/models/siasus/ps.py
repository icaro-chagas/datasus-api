from django.db import models

class PSSiasus(models.Model):
    cnes_exec = models.CharField(max_length=20, null=True)
    gestao = models.CharField(max_length=20, null=True)
    condic = models.CharField(max_length=20, null=True)
    ufmun = models.CharField(max_length=20, null=True)
    tpups = models.CharField(max_length=20, null=True)
    tippre = models.CharField(max_length=20, null=True)
    mn_ind = models.CharField(max_length=20, null=True)
    cnpjcpf = models.CharField(max_length=20, null=True)
    cnpjmnt = models.CharField(max_length=20, null=True)
    dt_process = models.CharField(max_length=20, null=True)
    dt_atend = models.CharField(max_length=20, null=True)
    cns_pac = models.CharField(max_length=20, null=True)
    dtnasc = models.CharField(max_length=20, null=True)
    tpidadepac = models.CharField(max_length=20, null=True)
    idadepac = models.CharField(max_length=20, null=True)
    nacion_pac = models.CharField(max_length=20, null=True)
    sexopac = models.CharField(max_length=20, null=True)
    racacor = models.CharField(max_length=20, null=True)
    etnia = models.CharField(max_length=20, null=True)
    munpac = models.CharField(max_length=20, null=True)
    mot_cob = models.CharField(max_length=20, null=True)
    dt_motcob = models.CharField(max_length=20, null=True)
    catend = models.CharField(max_length=20, null=True)
    cidpri = models.CharField(max_length=20, null=True)
    cidassoc = models.CharField(max_length=20, null=True)
    origem_pac = models.CharField(max_length=20, null=True)
    dt_inicio = models.CharField(max_length=20, null=True)
    dt_fim = models.CharField(max_length=20, null=True)
    cob_esf = models.CharField(max_length=20, null=True)
    cnes_esf = models.CharField(max_length=20, null=True)
    destinopac = models.CharField(max_length=20, null=True)
    pa_proc_id = models.CharField(max_length=20, null=True)
    pa_qtdpro = models.IntegerField(null=True)
    pa_qtdapr = models.IntegerField(null=True)
    pa_srv = models.CharField(max_length=20, null=True)
    pa_class_s = models.CharField(max_length=20, null=True)
    sit_rua = models.CharField(max_length=20, null=True)
    tp_droga = models.CharField(max_length=20, null=True)
    loc_realiz = models.CharField(max_length=20, null=True)
    inicio = models.CharField(max_length=20, null=True)
    fim = models.CharField(max_length=20, null=True)
    permanen = models.CharField(max_length=20, null=True)
    qtdate = models.CharField(max_length=20, null=True)
    qtdpcn = models.CharField(max_length=20, null=True)
    nat_jur = models.CharField(max_length=20, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)


    class Meta:
        db_table = 'ps_siasus'

        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]