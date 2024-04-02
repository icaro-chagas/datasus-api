from django.db import models

class PCE(models.Model):
    id_uf = models.CharField(max_length=25, null=True)
    sg_uf = models.CharField(max_length=25, null=True)
    id_distr = models.CharField(max_length=25, null=True)
    id_loc = models.CharField(max_length=25, null=True)
    dt_comp = models.CharField(max_length=25, null=True)
    qt_pop = models.CharField(max_length=25, null=True)
    qt_pred = models.CharField(max_length=25, null=True)
    qt_exam = models.CharField(max_length=25, null=True)
    qt_nrecol = models.CharField(max_length=25, null=True)
    qt_1a4 = models.CharField(max_length=25, null=True)
    qt_5a16 = models.CharField(max_length=25, null=True)
    qt_17 = models.CharField(max_length=25, null=True)
    qt_pos = models.CharField(max_length=25, null=True)
    qt_atrat = models.CharField(max_length=25, null=True)
    qt_trat = models.CharField(max_length=25, null=True)
    qt_ci = models.CharField(max_length=25, null=True)
    qt_rec = models.CharField(max_length=25, null=True)
    qt_aus = models.CharField(max_length=25, null=True)
    qt_asc = models.CharField(max_length=25, null=True)
    qt_anc = models.CharField(max_length=25, null=True)
    qt_tae = models.CharField(max_length=25, null=True)
    qt_tt = models.CharField(max_length=25, null=True)
    qt_ev = models.CharField(max_length=25, null=True)
    qt_se = models.CharField(max_length=25, null=True)
    qt_hn = models.CharField(max_length=25, null=True)
    qt_out = models.CharField(max_length=25, null=True)
    qt_cap = models.CharField(max_length=25, null=True)
    qt_pesq = models.CharField(max_length=25, null=True)
    qt_bgla = models.CharField(max_length=25, null=True)
    qt_bstr = models.CharField(max_length=25, null=True)
    qt_bten = models.CharField(max_length=25, null=True)
    qt_out1 = models.CharField(max_length=25, null=True)
    qt_posbgla = models.CharField(max_length=25, null=True)
    qt_posbten = models.CharField(max_length=25, null=True)
    qt_posbstr = models.CharField(max_length=25, null=True)
    qt_posout = models.CharField(max_length=25, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)

    class Meta:
        db_table = 'pce'
        indexes = [
            models.Index(fields=['uf', 'ano']),
        ]