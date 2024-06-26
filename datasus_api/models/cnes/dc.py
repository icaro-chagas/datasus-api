from django.db import models

class DCCnes(models.Model):
    cnes = models.CharField(max_length=7, null=True)
    codufmun = models.CharField(max_length=7, null=True)
    cpf_cnpj = models.CharField(max_length=14, null=True)
    pf_pj = models.CharField(max_length=1, null=True)
    niv_dep = models.CharField(max_length=1, null=True)
    cnpj_man = models.CharField(max_length=14, null=True)
    cod_ir = models.CharField(max_length=2, null=True)
    regsaude = models.CharField(max_length=4, null=True)
    micr_reg = models.CharField(max_length=6, null=True)
    distrsan = models.CharField(max_length=4, null=True)
    vinc_sus = models.CharField(max_length=1, null=True)
    distradm = models.CharField(max_length=4, null=True)
    tpgestao = models.CharField(max_length=1, null=True)
    esfera_a = models.CharField(max_length=2, null=True)
    retencao = models.CharField(max_length=2, null=True)
    atividad = models.CharField(max_length=2, null=True)
    natureza = models.CharField(max_length=2, null=True)
    clientel = models.CharField(max_length=2, null=True)
    tp_unid = models.CharField(max_length=2, null=True)
    turno_at = models.CharField(max_length=2, null=True)
    niv_hier = models.CharField(max_length=2, null=True)
    tp_prest = models.CharField(max_length=2, null=True)
    s_hbsagp = models.IntegerField(null=True)
    s_hbsagn = models.IntegerField(null=True)
    s_dpi = models.IntegerField(null=True)
    s_dpac = models.IntegerField(null=True)
    s_reagp = models.IntegerField(null=True)
    s_reagn = models.IntegerField(null=True)
    s_rehcv = models.IntegerField(null=True)
    maq_prop = models.IntegerField(null=True)
    maq_outr = models.IntegerField(null=True)
    f_areia = models.CharField(max_length=1, null=True)
    f_carvao = models.CharField(max_length=1, null=True)
    abrandad = models.CharField(max_length=1, null=True)
    deioniza = models.CharField(max_length=1, null=True)
    osmose_r = models.CharField(max_length=1, null=True)
    out_trat = models.CharField(max_length=1, null=True)
    cns_nefr = models.CharField(max_length=15, null=True)
    dialise = models.CharField(max_length=1, null=True)
    simul_rd = models.IntegerField(null=True)
    planj_rd = models.IntegerField(null=True)
    armaz_ft = models.IntegerField(null=True)
    conf_mas = models.IntegerField(null=True)
    sala_mol = models.IntegerField(null=True)
    blocoper = models.IntegerField(null=True)
    s_armaze = models.IntegerField(null=True)
    s_prepar = models.IntegerField(null=True)
    s_qcdura = models.IntegerField(null=True)
    s_qldura = models.IntegerField(null=True)
    s_cpflux = models.IntegerField(null=True)
    s_simula = models.IntegerField(null=True)
    s_acell6 = models.IntegerField(null=True)
    s_alseme = models.IntegerField(null=True)
    s_alcome = models.IntegerField(null=True)
    ortv1050 = models.IntegerField(null=True)
    orv50150 = models.IntegerField(null=True)
    ov150500 = models.IntegerField(null=True)
    un_cobal = models.IntegerField(null=True)
    eqbrbaix = models.IntegerField(null=True)
    eqbrmedi = models.IntegerField(null=True)
    eqbralta = models.IntegerField(null=True)
    eq_marea = models.IntegerField(null=True)
    eq_mindi = models.IntegerField(null=True)
    eqsispln = models.IntegerField(null=True)
    eqdoscli = models.IntegerField(null=True)
    eqfonsel = models.IntegerField(null=True)
    cns_adm = models.CharField(max_length=15, null=True)
    cns_oped = models.CharField(max_length=15, null=True)
    cns_conc = models.CharField(max_length=15, null=True)
    cns_oclin = models.CharField(max_length=15, null=True)
    cns_mrad = models.CharField(max_length=15, null=True)
    cns_fnuc = models.CharField(max_length=15, null=True)
    quimradi = models.CharField(max_length=1, null=True)
    s_recepc = models.IntegerField(null=True)
    s_trihmt = models.IntegerField(null=True)
    s_tricli = models.IntegerField(null=True)
    s_coleta = models.IntegerField(null=True)
    s_aferes = models.IntegerField(null=True)
    s_preest = models.IntegerField(null=True)
    s_proces = models.IntegerField(null=True)
    s_estoqu = models.IntegerField(null=True)
    s_distri = models.IntegerField(null=True)
    s_sorolo = models.IntegerField(null=True)
    s_imunoh = models.IntegerField(null=True)
    s_pretra = models.IntegerField(null=True)
    s_hemost = models.IntegerField(null=True)
    s_contrq = models.IntegerField(null=True)
    s_biomol = models.IntegerField(null=True)
    s_imunfe = models.IntegerField(null=True)
    s_transf = models.IntegerField(null=True)
    s_sgdoad = models.IntegerField(null=True)
    qt_cadre = models.IntegerField(null=True)
    qt_cenre = models.IntegerField(null=True)
    qt_refsa = models.IntegerField(null=True)
    qt_conra = models.IntegerField(null=True)
    qt_extpl = models.IntegerField(null=True)
    qt_fre18 = models.IntegerField(null=True)
    qt_fre30 = models.IntegerField(null=True)
    qt_agipl = models.IntegerField(null=True)
    qt_selad = models.IntegerField(null=True)
    qt_irrhe = models.IntegerField(null=True)
    qt_agltn = models.IntegerField(null=True)
    qt_maqaf = models.IntegerField(null=True)
    qt_refre = models.IntegerField(null=True)
    qt_refas = models.IntegerField(null=True)
    qt_capfl = models.IntegerField(null=True)
    cns_hmtr = models.CharField(max_length=15, null=True)
    cns_hmtl = models.CharField(max_length=15, null=True)
    cns_cres = models.CharField(max_length=15, null=True)
    cns_rtec = models.CharField(max_length=15, null=True)
    hemotera = models.CharField(max_length=1, null=True)
    ap01cv01 = models.CharField(max_length=1, null=True)
    ap01cv02 = models.CharField(max_length=1, null=True)
    ap01cv03 = models.CharField(max_length=1, null=True)
    ap01cv04 = models.CharField(max_length=1, null=True)
    ap01cv05 = models.CharField(max_length=1, null=True)
    ap01cv06 = models.CharField(max_length=1, null=True)
    ap01cv07 = models.CharField(max_length=1, null=True)
    ap02cv01 = models.CharField(max_length=1, null=True)
    ap02cv02 = models.CharField(max_length=1, null=True)
    ap02cv03 = models.CharField(max_length=1, null=True)
    ap02cv04 = models.CharField(max_length=1, null=True)
    ap02cv05 = models.CharField(max_length=1, null=True)
    ap02cv06 = models.CharField(max_length=1, null=True)
    ap02cv07 = models.CharField(max_length=1, null=True)
    ap03cv01 = models.CharField(max_length=1, null=True)
    ap03cv02 = models.CharField(max_length=1, null=True)
    ap03cv03 = models.CharField(max_length=1, null=True)
    ap03cv04 = models.CharField(max_length=1, null=True)
    ap03cv05 = models.CharField(max_length=1, null=True)
    ap03cv06 = models.CharField(max_length=1, null=True)
    ap03cv07 = models.CharField(max_length=1, null=True)
    ap04cv01 = models.CharField(max_length=1, null=True)
    ap04cv02 = models.CharField(max_length=1, null=True)
    ap04cv03 = models.CharField(max_length=1, null=True)
    ap04cv04 = models.CharField(max_length=1, null=True)
    ap04cv05 = models.CharField(max_length=1, null=True)
    ap04cv06 = models.CharField(max_length=1, null=True)
    ap04cv07 = models.CharField(max_length=1, null=True)
    ap05cv01 = models.CharField(max_length=1, null=True)
    ap05cv02 = models.CharField(max_length=1, null=True)
    ap05cv03 = models.CharField(max_length=1, null=True)
    ap05cv04 = models.CharField(max_length=1, null=True)
    ap05cv05 = models.CharField(max_length=1, null=True)
    ap05cv06 = models.CharField(max_length=1, null=True)
    ap05cv07 = models.CharField(max_length=1, null=True)
    ap06cv01 = models.CharField(max_length=1, null=True)
    ap06cv02 = models.CharField(max_length=1, null=True)
    ap06cv03 = models.CharField(max_length=1, null=True)
    ap06cv04 = models.CharField(max_length=1, null=True)
    ap06cv05 = models.CharField(max_length=1, null=True)
    ap06cv06 = models.CharField(max_length=1, null=True)
    ap06cv07 = models.CharField(max_length=1, null=True)
    ap07cv01 = models.CharField(max_length=1, null=True)
    ap07cv02 = models.CharField(max_length=1, null=True)
    ap07cv03 = models.CharField(max_length=1, null=True)
    ap07cv04 = models.CharField(max_length=1, null=True)
    ap07cv05 = models.CharField(max_length=1, null=True)
    ap07cv06 = models.CharField(max_length=1, null=True)
    ap07cv07 = models.CharField(max_length=1, null=True)
    atend_pr = models.CharField(max_length=1, null=True)
    gesprg3e = models.CharField(max_length=1, null=True)
    gesprg3m = models.CharField(max_length=1, null=True)
    gesprg4e = models.CharField(max_length=1, null=True)
    gesprg4m = models.CharField(max_length=1, null=True)
    gesprg6e = models.CharField(max_length=1, null=True)
    gesprg6m = models.CharField(max_length=1, null=True)
    nivate_a = models.CharField(max_length=1, null=True)
    nivate_h = models.CharField(max_length=1, null=True)
    competen = models.CharField(max_length=6, null=True)
    nat_jur = models.CharField(max_length=4, null=True)
    uf = models.CharField(max_length=30, db_index=True)
    ano = models.CharField(max_length=30, db_index=True)
    mes = models.CharField(max_length=30, db_index=True)

    class Meta:
        db_table = 'dc_cnes'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]