from django.db import models

class ACFSiasus(models.Model):
    ap_mvm = models.CharField(max_length=20, null=True)
    ap_condic = models.CharField(max_length=20, null=True)
    ap_gestao = models.CharField(max_length=20, null=True)
    ap_coduni = models.CharField(max_length=20, null=True)
    ap_autoriz = models.CharField(max_length=20, null=True)
    ap_cmp = models.CharField(max_length=20, null=True)
    ap_pripal = models.CharField(max_length=20, null=True)
    ap_vl_ap = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    ap_ufmun = models.CharField(max_length=20, null=True)
    ap_tpups = models.CharField(max_length=20, null=True)
    ap_tippre = models.CharField(max_length=20, null=True)
    ap_mn_ind = models.CharField(max_length=20, null=True)
    ap_cnpjcpf = models.CharField(max_length=20, null=True)
    ap_cnpjmnt = models.CharField(max_length=20, null=True)
    ap_cnspcn = models.CharField(max_length=20, null=True)
    ap_coidade = models.CharField(max_length=20, null=True)
    ap_nuidade = models.CharField(max_length=20, null=True)
    ap_sexo = models.CharField(max_length=20, null=True)
    ap_racacor = models.CharField(max_length=20, null=True)
    ap_munpcn = models.CharField(max_length=20, null=True)
    ap_ufnacio = models.CharField(max_length=20, null=True)
    ap_ceppcn = models.CharField(max_length=20, null=True)
    ap_ufdif = models.CharField(max_length=20, null=True)
    ap_mndif = models.CharField(max_length=20, null=True)
    ap_dtinic = models.CharField(max_length=20, null=True)
    ap_dtfim = models.CharField(max_length=20, null=True)
    ap_tpaten = models.CharField(max_length=20, null=True)
    ap_tpapac = models.CharField(max_length=20, null=True)
    ap_motsai = models.CharField(max_length=20, null=True)
    ap_obito = models.CharField(max_length=20, null=True)
    ap_encerr = models.CharField(max_length=20, null=True)
    ap_perman = models.CharField(max_length=20, null=True)
    ap_alta = models.CharField(max_length=20, null=True)
    ap_transf = models.CharField(max_length=20, null=True)
    ap_dtocor = models.CharField(max_length=20, null=True)
    ap_codemi = models.CharField(max_length=20, null=True)
    ap_catend = models.CharField(max_length=20, null=True)
    ap_apacant = models.CharField(max_length=20, null=True)
    ap_unisol = models.CharField(max_length=20, null=True)
    ap_dtsolic = models.CharField(max_length=20, null=True)
    ap_dtaut = models.CharField(max_length=20, null=True)
    ap_cidcas = models.CharField(max_length=20, null=True)
    ap_cidpri = models.CharField(max_length=20, null=True)
    ap_cidsec = models.CharField(max_length=20, null=True)
    ap_etnia = models.CharField(max_length=20, null=True)
    acf_duplex = models.CharField(max_length=20, null=True)
    acf_usocat = models.CharField(max_length=20, null=True)
    acf_prefav = models.CharField(max_length=20, null=True)
    acf_flebit = models.CharField(max_length=20, null=True)
    acf_hemato = models.CharField(max_length=20, null=True)
    acf_veiavi = models.CharField(max_length=20, null=True)
    acf_pulso = models.CharField(max_length=20, null=True)
    acf_veidia = models.IntegerField(null=True)
    acf_artdia = models.IntegerField(null=True)
    acf_fremit = models.CharField(max_length=20, null=True)
    ap_natjur = models.CharField(max_length=20, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)


    class Meta:
        db_table = 'acf_siasus'

        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]