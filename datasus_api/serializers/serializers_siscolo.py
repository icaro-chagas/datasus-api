from rest_framework import serializers
from ..models.siscolo.cc import CCSiscolo
from ..models.siscolo.hc import HCSiscolo


class CCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCSiscolo
        fields = ['co_us', 'co_us_uf', 'co_us_ibge', 'regus', 'co_pac_ibg', 'co_pac_uf', 'co_pac_esc',
                  'co_res_nor', 'co_pac_ida', 'regresid', 'co_cnes', 'clabibge', 'clabuf', 'reglab',
                  'dt_id_comp', 'ano_comp', 'co_fx_etar', 'co_pac_rac', 'co_ati_esc', 'co_ati_gla',
                  'co_ati_ind', 'co_cel_esc', 'co_cel_gla', 'co_neo_mal', 'co_amostra', 'co_adeq_ma',
                  'co_ben_inf', 'co_ben_met', 'co_ben_rep', 'co_ben_atr', 'co_ben_rad', 'co_ben_out',
                  'co_mic_lac', 'co_mic_coc', 'co_mic_chl', 'co_mic_act', 'co_mic_bac', 'co_mic_tri',
                  'co_mic_her', 'co_mic_can', 'co_mic_gar', 'co_mic_out', 'co_anm_pre', 'dt_anm_pre',
                  'st_mon_ext', 'tempcitant', 'dintcoleta', 'dintresult', 'dinttempex', 'qtdexa',
                  'reprezt', 'resnorm', 'posnaoneo', 'lesaltgra', 'psnaonpla', 'nlsaltgra', 'psnnpla',
                  'naltgra', 'lbgrau', 'lagrau', 'lagraumi', 'carcino', 'c_epi_esca', 'c_epi_glan',
                  'co_epi_met', 'adencarcin', 'dencarcinv', 'outneo', 'alterado', 'cvcional', 'meioliqu',
                  'amosrejaus', 'amosrejdan', 'amosrejalh', 'amosrejout', 'rejeitada', 'satisfact',
                  'insatsfac', 'co_insa_ac', 'co_insa_sa', 'co_insa_pi', 'co_insa_ar', 'co_insa_co',
                  'co_insa_su', 'co_insa_ou', 'cbeminfla', 'cbemmetas', 'cbemrepar', 'cbematrof',
                  'cbemradi', 'cbemout', 'cmiclact', 'cmiccoco', 'cmicchla', 'cmicacti', 'cmicbaci',
                  'cmictrico', 'cmicherp', 'cmiccand', 'cmicgard', 'cmicout', 'uf', 'ano', 'mes']


class HCSerializer(serializers.ModelSerializer):
    class Meta:
        model = HCSiscolo
        fields = ['co_us', 'co_us_uf', 'co_us_ibge', 'regus', 'co_pac_ibg', 'co_pac_uf', 'co_pac_esc',
                  'dt_pac_nas', 'co_pac_ida', 'regresid', 'co_cnes', 'clabibge', 'clabuf', 'clabcid',
                  'reglab', 'dt_id_comp', 'ano_comp', 'co_fx_etar', 'co_pac_rac', 'co_cit_esc', 'co_cit_gla',
                  'co_cit_ind', 'o_cit_esca', 'o_cit_glan', 'co_colp', 'co_res_tip', 'co_res_loc',
                  'co_ben_cer', 'co_ben_alt', 'co_neo_nic', 'co_neo_ade', 'co_dif_gra', 'co_exten_p',
                  'co_exten_v', 'o_exten_pe', 'o_exten_pa', 'co_exten_c', 'o_exten_va', 'co_marg',
                  'co_res_fra', 'co_res_tam', 'o_res_tam2', 'co_res_mar', 'dt_his_exa', 'dt_his_rec',
                  'co_mat_ins', 'co_ctrl_fr', 'co_ctrl_bl', 'qtdexa', 'dintcoleta', 'dintresult', 'dinttempex',
                  'escamosa', 'pneopla', 'gpnneop', 'gnaltgrau', 'indpnaoneo', 'citindalgr', 'esclipbx',
                  'escinalt', 'esciemcinv', 'esccarinva', 'adenoinsut', 'adencarcin', 'cit_outneo',
                  'ccoldefaul', 'ccolnormal', 'ccolanorma', 'ccolinsati', 'co_colp_po', 'o_colp_pos',
                  'co_colp_bi', 'co_colp_cu', 'co_colp_ex', 'co_colp_re', 'o_colp_bio', 'cresbiopsi',
                  'cresconiza', 'creshissim', 'crespanhis', 'cresoutros', 'cresecto', 'cresendo', 'cresjunc',
                  'co_ben_met', 'co_ben_pol', 'cbencervi', 'cbenalter', 'nicdleve', 'nicdmode', 'nicdacent',
                  'niccarcmin', 'nicepiinva', 'nicimpaval', 'nicverruco', 'nicnaocera', 'neoinsutu', 'neomucino',
                  'neovilogl', 'ds_neo_out', 'cdifgrau', 'cdifmoddif', 'cdifpoudif', 'cdifindfer', 'cdiexamins',
                  'c_ext_vasc', 'c_ext_peri', 'c_ext_para', 'c_ext_corp', 'c_ext_vagi', 'co_exten_l',
                  'o_exten_li', 'cmarlivre', 'cmarcompro', 'cmarimpava', 'uf', 'ano', 'mes']
        


