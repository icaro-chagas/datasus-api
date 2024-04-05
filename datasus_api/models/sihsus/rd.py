from django.db import models

class RDSihsus(models.Model):
    uf_zi = models.CharField(max_length=60, null=True)
    ano_cmpt = models.CharField(max_length=60, null=True)
    mes_cmpt = models.CharField(max_length=60, null=True)
    espec = models.CharField(max_length=60, null=True)
    cgc_hosp = models.CharField(max_length=60, null=True)
    n_aih = models.CharField(max_length=60, null=True)
    ident = models.CharField(max_length=60, null=True)
    cep = models.CharField(max_length=60, null=True)
    munic_res = models.CharField(max_length=60, null=True)
    nasc = models.CharField(max_length=60, null=True)
    sexo = models.CharField(max_length=60, null=True)
    uti_mes_in = models.IntegerField(null=True)
    uti_mes_an = models.IntegerField(null=True)
    uti_mes_al = models.IntegerField(null=True)
    uti_mes_to = models.IntegerField(null=True)
    marca_uti = models.CharField(max_length=60, null=True)
    uti_int_in = models.IntegerField(null=True)
    uti_int_an = models.IntegerField(null=True)
    uti_int_al = models.IntegerField(null=True)
    uti_int_to = models.IntegerField(null=True)
    diar_acom = models.IntegerField(null=True)
    qt_diarias = models.IntegerField(null=True)
    proc_solic = models.CharField(max_length=60, null=True)
    proc_rea = models.CharField(max_length=60, null=True)
    val_sh = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_sp = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_sadt = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_rn = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_acomp = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_ortp = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_sangue = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_sadtsr = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    val_transp = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    val_obsang = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    val_ped1ac = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    val_tot = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    val_uti = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    us_tot = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dt_inter = models.CharField(max_length=60, null=True)
    dt_saida = models.CharField(max_length=60, null=True)
    diag_princ = models.CharField(max_length=60, null=True)
    diag_secun = models.CharField(max_length=60, null=True)
    cobranca = models.CharField(max_length=60, null=True)
    natureza = models.CharField(max_length=60, null=True)
    nat_jur = models.CharField(max_length=60, null=True)
    gestao = models.CharField(max_length=60, null=True)
    rubrica = models.IntegerField(null=True)
    ind_vdrl = models.CharField(max_length=60, null=True)
    munic_mov = models.CharField(max_length=60, null=True)
    cod_idade = models.CharField(max_length=60, null=True)
    idade = models.IntegerField(null=True)
    dias_perm = models.IntegerField(null=True)
    morte = models.IntegerField(null=True)
    nacional = models.CharField(max_length=60, null=True)
    num_proc = models.CharField(max_length=60, null=True)
    car_int = models.CharField(max_length=60, null=True)
    tot_pt_sp = models.IntegerField(null=True)
    cpf_aut = models.CharField(max_length=60, null=True)
    homonimo = models.CharField(max_length=60, null=True)
    num_filhos = models.IntegerField(null=True)
    instru = models.CharField(max_length=60, null=True)
    cid_notif = models.CharField(max_length=60, null=True)
    contracep1 = models.CharField(max_length=60, null=True)
    contracep2 = models.CharField(max_length=60, null=True)
    gestrisco = models.CharField(max_length=60, null=True)
    insc_pn = models.CharField(max_length=60, null=True)
    seq_aih5 = models.CharField(max_length=60, null=True)
    cbor = models.CharField(max_length=60, null=True)
    cnaer = models.CharField(max_length=60, null=True)
    vincprev = models.CharField(max_length=60, null=True)
    gestor_cod = models.CharField(max_length=60, null=True)
    gestor_tp = models.CharField(max_length=60, null=True)
    gestor_cpf = models.CharField(max_length=60, null=True)
    gestor_dt = models.CharField(max_length=60, null=True)
    cnes = models.CharField(max_length=60, null=True)
    cnpj_mant = models.CharField(max_length=60, null=True)
    infehosp = models.CharField(max_length=60, null=True)
    cid_asso = models.CharField(max_length=60, null=True)
    cid_morte = models.CharField(max_length=60, null=True)
    complex = models.CharField(max_length=60, null=True)
    financ = models.CharField(max_length=60, null=True)
    faec_tp = models.CharField(max_length=60, null=True)
    regct = models.CharField(max_length=60, null=True)
    raca_cor = models.CharField(max_length=60, null=True)
    etnia = models.CharField(max_length=60, null=True)
    sequencia = models.IntegerField(null=True)
    remessa = models.CharField(max_length=60, null=True)
    aud_just = models.CharField(max_length=60, null=True)
    sis_just = models.CharField(max_length=60, null=True)
    val_sh_fed = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    val_sp_fed = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    val_sh_ges = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    val_sp_ges = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    val_uci = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    marca_uci = models.CharField(max_length=60, null=True)
    diagsec1 = models.CharField(max_length=60, null=True)
    diagsec2 = models.CharField(max_length=60, null=True)
    diagsec3 = models.CharField(max_length=60, null=True)
    diagsec4 = models.CharField(max_length=60, null=True)
    diagsec5 = models.CharField(max_length=60, null=True)
    diagsec6 = models.CharField(max_length=60, null=True)
    diagsec7 = models.CharField(max_length=60, null=True)
    diagsec8 = models.CharField(max_length=60, null=True)
    diagsec9 = models.CharField(max_length=60, null=True)
    tpdisec1 = models.CharField(max_length=60, null=True)
    tpdisec2 = models.CharField(max_length=60, null=True)
    tpdisec3 = models.CharField(max_length=60, null=True)
    tpdisec4 = models.CharField(max_length=60, null=True)
    tpdisec5 = models.CharField(max_length=60, null=True)
    tpdisec6 = models.CharField(max_length=60, null=True)
    tpdisec7 = models.CharField(max_length=60, null=True)
    tpdisec8 = models.CharField(max_length=60, null=True)
    tpdisec9 = models.CharField(max_length=60, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)


    class Meta:
        db_table = 'rd_sihsus'

        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]