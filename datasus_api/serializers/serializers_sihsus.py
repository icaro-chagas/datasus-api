from rest_framework import serializers
from ..models.sihsus.er import ERSihsus
from ..models.sihsus.rd import RDSihsus
from ..models.sihsus.rj import RJSihsus
from ..models.sihsus.sp import SPSihsus


class ERSerializer(serializers.ModelSerializer):
    class Meta:
        model = ERSihsus
        fields = ['sequencia', 'remessa', 'cnes', 'aih', 'ano', 'mes', 'dt_inter', 'dt_saida', 'mun_mov',
                  'uf_zi', 'mun_res', 'uf_res', 'co_erro', 'uf', 'ano', 'mes']
        

class RDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RDSihsus
        fields = ['uf_zi', 'ano_cmpt', 'mes_cmpt', 'espec', 'cgc_hosp', 'n_aih', 'ident', 'cep', 'munic_res', 'nasc',
           'sexo', 'uti_mes_in', 'uti_mes_an', 'uti_mes_al', 'uti_mes_to', 'marca_uti', 'uti_int_in', 'uti_int_an',
           'uti_int_al', 'uti_int_to', 'diar_acom', 'qt_diarias', 'proc_solic', 'proc_rea', 'val_sh', 'val_sp',
           'val_sadt', 'val_rn', 'val_acomp', 'val_ortp', 'val_sangue', 'val_sadtsr', 'val_transp', 'val_obsang',
           'val_ped1ac', 'val_tot', 'val_uti', 'us_tot', 'dt_inter', 'dt_saida', 'diag_princ', 'diag_secun',
           'cobranca', 'natureza', 'nat_jur', 'gestao', 'rubrica', 'ind_vdrl', 'munic_mov', 'cod_idade', 'idade',
           'dias_perm', 'morte', 'nacional', 'num_proc', 'car_int', 'tot_pt_sp', 'cpf_aut', 'homonimo', 'num_filhos',
           'instru', 'cid_notif', 'contracep1', 'contracep2', 'gestrisco', 'insc_pn', 'seq_aih5', 'cbor', 'cnaer',
           'vincprev', 'gestor_cod', 'gestor_tp', 'gestor_cpf', 'gestor_dt', 'cnes', 'cnpj_mant', 'infehosp',
           'cid_asso', 'cid_morte', 'complex', 'financ', 'faec_tp', 'regct', 'raca_cor', 'etnia', 'sequencia',
           'remessa', 'aud_just', 'sis_just', 'val_sh_fed', 'val_sp_fed', 'val_sh_ges', 'val_sp_ges', 'val_uci',
           'marca_uci', 'diagsec1', 'diagsec2', 'diagsec3', 'diagsec4', 'diagsec5', 'diagsec6', 'diagsec7', 'diagsec8',
           'diagsec9', 'tpdisec1', 'tpdisec2', 'tpdisec3', 'tpdisec4', 'tpdisec5', 'tpdisec6', 'tpdisec7', 'tpdisec8',
           'tpdisec9', 'uf', 'ano', 'mes']
        

class RJSerializer(serializers.ModelSerializer):
    class Meta:
        model = RJSihsus
        fields = ['uf_zi', 'ano_cmpt', 'mes_cmpt', 'espec', 'cgc_hosp', 'n_aih', 'ident', 'cep', 'munic_res', 'nasc',
           'sexo', 'uti_mes_in', 'uti_mes_an', 'uti_mes_al', 'uti_mes_to', 'marca_uti', 'uti_int_in', 'uti_int_an',
           'uti_int_al', 'uti_int_to', 'diar_acom', 'qt_diarias', 'proc_solic', 'proc_rea', 'val_sh', 'val_sp', 'val_sadt',
           'val_rn', 'val_acomp', 'val_ortp', 'val_sangue', 'val_sadtsr', 'val_transp', 'val_obsang', 'val_ped1ac', 'val_tot',
           'val_uti', 'us_tot', 'dt_inter', 'dt_saida', 'diag_princ', 'diag_secun', 'cobranca', 'natureza', 'nat_jur', 'gestao',
           'rubrica', 'ind_vdrl', 'munic_mov', 'cod_idade', 'idade', 'dias_perm', 'morte', 'nacional', 'num_proc', 'car_int',
           'tot_pt_sp', 'cpf_aut', 'homonimo', 'num_filhos', 'instru', 'cid_notif', 'contracep1', 'contracep2', 'gestrisco',
           'insc_pn', 'seq_aih5', 'cbor', 'cnaer', 'vincprev', 'gestor_cod', 'gestor_tp', 'gestor_cpf', 'gestor_dt', 'cnes',
           'cnpj_mant', 'infehosp', 'cid_asso', 'cid_morte', 'complex', 'financ', 'faec_tp', 'regct', 'raca_cor', 'etnia',
           'st_situac', 'st_bloq', 'st_mot_blo', 'sequencia', 'remessa', 'uf', 'ano', 'mes']
        

class SPSializer(serializers.ModelSerializer):
    class Meta:
        model = SPSihsus
        fields = ['sp_gestor', 'sp_uf', 'sp_aa', 'sp_mm', 'sp_cnes', 'sp_naih', 'sp_procrea', 'sp_dtinter',
           'sp_dtsaida', 'sp_num_pr', 'sp_tipo', 'sp_cpfcgc', 'sp_atoprof', 'sp_tp_ato', 'sp_qtd_ato',
           'sp_ptsp', 'sp_nf', 'sp_valato', 'sp_m_hosp', 'sp_m_pac', 'sp_des_hos', 'sp_des_pac', 'sp_complex',
           'sp_financ', 'sp_co_faec', 'sp_pf_cbo', 'sp_pf_doc', 'sp_pj_doc', 'in_tp_val', 'sequencia', 'remessa',
           'serv_cla', 'sp_cidpri', 'sp_cidsec', 'sp_qt_proc', 'sp_u_aih', 'uf', 'ano', 'mes']

        

