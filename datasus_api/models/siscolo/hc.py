from django.db import models

class HCSiscolo(models.Model):
    co_us = models.CharField(max_length=60, null=True)
    co_us_uf = models.CharField(max_length=60, null=True)
    co_us_ibge = models.CharField(max_length=60, null=True)
    regus = models.CharField(max_length=60, null=True)
    co_pac_ibg = models.CharField(max_length=60, null=True)
    co_pac_uf = models.CharField(max_length=60, null=True)
    co_pac_esc = models.CharField(max_length=60, null=True)
    dt_pac_nas = models.CharField(max_length=60, null=True)
    co_pac_ida = models.CharField(max_length=60, null=True)
    regresid = models.CharField(max_length=60, null=True)
    co_cnes = models.CharField(max_length=60, null=True)
    clabibge = models.CharField(max_length=60, null=True)
    clabuf = models.CharField(max_length=60, null=True)
    clabcid = models.CharField(max_length=60, null=True)
    reglab = models.CharField(max_length=60, null=True)
    dt_id_comp = models.CharField(max_length=60, null=True)
    ano_comp = models.CharField(max_length=60, null=True)
    co_fx_etar = models.CharField(max_length=60, null=True)
    co_pac_rac = models.CharField(max_length=60, null=True)
    co_cit_esc = models.CharField(max_length=60, null=True)
    co_cit_gla = models.CharField(max_length=60, null=True)
    co_cit_ind = models.CharField(max_length=60, null=True)
    o_cit_esca = models.CharField(max_length=60, null=True)
    o_cit_glan = models.CharField(max_length=60, null=True)
    co_colp = models.CharField(max_length=60, null=True)
    co_res_tip = models.CharField(max_length=60, null=True)
    co_res_loc = models.CharField(max_length=60, null=True)
    co_ben_cer = models.CharField(max_length=60, null=True)
    co_ben_alt = models.CharField(max_length=60, null=True)
    co_neo_nic = models.CharField(max_length=60, null=True)
    co_neo_ade = models.CharField(max_length=60, null=True)
    co_dif_gra = models.CharField(max_length=60, null=True)
    co_exten_p = models.CharField(max_length=60, null=True)
    co_exten_v = models.CharField(max_length=60, null=True)
    o_exten_pe = models.CharField(max_length=60, null=True)
    o_exten_pa = models.CharField(max_length=60, null=True)
    co_exten_c = models.CharField(max_length=60, null=True)
    o_exten_va = models.CharField(max_length=60, null=True)
    co_marg = models.CharField(max_length=60, null=True)
    co_res_fra = models.CharField(max_length=60, null=True)
    co_res_tam = models.CharField(max_length=60, null=True)
    o_res_tam2 = models.CharField(max_length=60, null=True)
    co_res_mar = models.CharField(max_length=60, null=True)
    dt_his_exa = models.CharField(max_length=60, null=True)
    dt_his_rec = models.CharField(max_length=60, null=True)
    co_mat_ins = models.CharField(max_length=60, null=True)
    co_ctrl_fr = models.CharField(max_length=60, null=True)
    co_ctrl_bl = models.CharField(max_length=60, null=True)
    qtdexa = models.CharField(max_length=60, null=True)
    dintcoleta = models.CharField(max_length=60, null=True)
    dintresult = models.CharField(max_length=60, null=True)
    dinttempex = models.CharField(max_length=60, null=True)
    escamosa = models.CharField(max_length=60, null=True)
    pneopla = models.CharField(max_length=60, null=True)
    gpnneop = models.CharField(max_length=60, null=True)
    gnaltgrau = models.CharField(max_length=60, null=True)
    indpnaoneo = models.CharField(max_length=60, null=True)
    citindalgr = models.CharField(max_length=60, null=True)
    esclipbx = models.CharField(max_length=60, null=True)
    escinalt = models.CharField(max_length=60, null=True)
    esciemcinv = models.CharField(max_length=60, null=True)
    esccarinva = models.CharField(max_length=60, null=True)
    adenoinsut = models.CharField(max_length=60, null=True)
    adencarcin = models.CharField(max_length=60, null=True)
    cit_outneo = models.CharField(max_length=60, null=True)
    ccoldefaul = models.CharField(max_length=60, null=True)
    ccolnormal = models.CharField(max_length=60, null=True)
    ccolanorma = models.CharField(max_length=60, null=True)
    ccolinsati = models.CharField(max_length=60, null=True)
    co_colp_po = models.CharField(max_length=60, null=True)
    o_colp_pos = models.CharField(max_length=60, null=True)
    co_colp_bi = models.CharField(max_length=60, null=True)
    co_colp_cu = models.CharField(max_length=60, null=True)
    co_colp_ex = models.CharField(max_length=60, null=True)
    co_colp_re = models.CharField(max_length=60, null=True)
    o_colp_bio = models.CharField(max_length=60, null=True)
    cresbiopsi = models.CharField(max_length=60, null=True)
    cresconiza = models.CharField(max_length=60, null=True)
    creshissim = models.CharField(max_length=60, null=True)
    crespanhis = models.CharField(max_length=60, null=True)
    cresoutros = models.CharField(max_length=60, null=True)
    cresecto = models.CharField(max_length=60, null=True)
    cresendo = models.CharField(max_length=60, null=True)
    cresjunc = models.CharField(max_length=60, null=True)
    co_ben_met = models.CharField(max_length=60, null=True)
    co_ben_pol = models.CharField(max_length=60, null=True)
    cbencervi = models.CharField(max_length=60, null=True)
    cbenalter = models.CharField(max_length=60, null=True)
    nicdleve = models.CharField(max_length=60, null=True)
    nicdmode = models.CharField(max_length=60, null=True)
    nicdacent = models.CharField(max_length=60, null=True)
    niccarcmin = models.CharField(max_length=60, null=True)
    nicepiinva = models.CharField(max_length=60, null=True)
    nicimpaval = models.CharField(max_length=60, null=True)
    nicverruco = models.CharField(max_length=60, null=True)
    nicnaocera = models.CharField(max_length=60, null=True)
    neoinsutu = models.CharField(max_length=60, null=True)
    neomucino = models.CharField(max_length=60, null=True)
    neovilogl = models.CharField(max_length=60, null=True)
    ds_neo_out = models.CharField(max_length=60, null=True)
    cdifgrau = models.CharField(max_length=60, null=True)
    cdifmoddif = models.CharField(max_length=60, null=True)
    cdifpoudif = models.CharField(max_length=60, null=True)
    cdifindfer = models.CharField(max_length=60, null=True)
    cdiexamins = models.CharField(max_length=60, null=True)
    c_ext_vasc = models.CharField(max_length=60, null=True)
    c_ext_peri = models.CharField(max_length=60, null=True)
    c_ext_para = models.CharField(max_length=60, null=True)
    c_ext_corp = models.CharField(max_length=60, null=True)
    c_ext_vagi = models.CharField(max_length=60, null=True)
    co_exten_l = models.CharField(max_length=60, null=True)
    o_exten_li = models.CharField(max_length=60, null=True)
    cmarlivre = models.CharField(max_length=60, null=True)
    cmarcompro = models.CharField(max_length=60, null=True)
    cmarimpava = models.CharField(max_length=60, null=True)
    uf = models.CharField(max_length=3, db_index=True)
    ano = models.CharField(max_length=4, db_index=True)
    mes = models.CharField(max_length=2, db_index=True)

    class Meta:
        db_table = 'hc_siscolo'
        indexes = [
            models.Index(fields=['uf', 'ano', 'mes']),
            models.Index(fields=['uf', 'ano']),
            models.Index(fields=['uf', 'mes']),
            models.Index(fields=['mes', 'ano'])
        ]