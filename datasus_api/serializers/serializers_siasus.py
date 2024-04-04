from rest_framework import serializers
from ..models.siasus.ab import ABSiasus
from ..models.siasus.abo import ABOSiasus
from ..models.siasus.acf import ACFSiasus
from ..models.siasus.ad import ADSiasus
from ..models.siasus.am import AMSiasus
from ..models.siasus.an import ANSiasus
from ..models.siasus.aq import AQSiasus
from ..models.siasus.ar import ARSiasus
from ..models.siasus.atd import ATDSiasus
from ..models.siasus.pa import PASiasus


        

class ABSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
                  'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
                  'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
                  'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
                  'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
                  'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'ab_imc', 'ab_procaih', 'ab_dtcirur',
                  'ab_numaih', 'ab_prcaih2', 'ab_prcaih3', 'ab_numaih2', 'ab_dtcirg2', 'ab_mesacom', 'ab_anoacom',
                  'ab_pontbar', 'ab_tabbarr', 'ap_natjur', 'uf', 'ano', 'mes']
        

class ABOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABOSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
                  'ap_ufmun', 'ap_tpups', 'ap_tppre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
                  'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
                  'ap_dtinic', 'ap_dtfim', 'ap_tpatend', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
                  'ap_alta', 'ap_transf', 'ap_dtoocor', 'ap_codemi', 'ap_catend', 'ap_apacan', 'ap_unisol', 'ap_dtsolic',
                  'ap_dtaut', 'ap_cidcas', 'co_cidprim', 'co_cidsec', 'ap_etnia', 'ab_imc', 'ab_procaih', 'ab_dtcirur',
                  'ab_numaih', 'ab_prcaih2', 'ab_t_prc2', 'ab_prcaih3', 'ab_t_prc3', 'ab_prcaih4', 'ab_t_prc4', 'ab_prcaih5',
                  'ab_t_prc5', 'ab_prcaih6', 'ab_t_prc6', 'ab_numaih2', 'ab_dtcirg2', 'ab_mesacom', 'ab_anoacom', 'ab_pontbar',
                  'ab_tabbarr', 'ap_comorb', 'ap_cid_c1', 'ap_cid_c2', 'ap_cid_c3', 'ap_cid_c4', 'ap_cid_c5', 'ap_cid_co',
                  'ap_medicam', 'ap_polivit', 'ap_atv_fis', 'ap_reg_pes', 'ap_adesao', 'ap_natjur', 'uf', 'ano', 'mes']
        

class ACFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACFSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
                  'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
                  'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
                  'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
                  'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
                  'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'acf_duplex', 'acf_usocat', 'acf_prefav',
                  'acf_flebit', 'acf_hemato', 'acf_veiavi', 'acf_pulso', 'acf_veidia', 'acf_artdia', 'acf_fremit',
                  'ap_natjur', 'uf', 'ano', 'mes']
        

class ADSerializer(serializers.ModelSerializer):
    class Meta:
        model = ADSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap', 'ap_ufmun',
           'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade', 'ap_nuidade',
           'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif', 'ap_dtinic', 'ap_dtfim',
           'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman', 'ap_alta', 'ap_transf', 'ap_dtocor',
           'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic', 'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec',
           'ap_etnia', 'ap_natjur', 'uf', 'ano', 'mes']
        

class AMSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
           'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
           'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
           'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
           'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
           'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'am_peso', 'am_altura', 'am_transpl',
           'am_qtdtran', 'am_gestant', 'ap_natjur', 'uf', 'ano', 'mes']


class ANSerializer(serializers.ModelSerializer):
    class Meta:
        model = ANSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
           'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
           'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
           'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
           'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
           'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'an_dtpdr', 'an_altura', 'an_peso', 'an_diures',
           'an_glicos', 'an_acevas', 'an_ulsoab', 'an_tru', 'an_intfis', 'an_cncdo', 'an_albumi', 'an_hcv', 'an_hbsag',
           'an_hiv', 'an_hb', 'uf', 'ano', 'mes']
        


class AQSerializer(serializers.ModelSerializer):
    class Meta:
        model = AQSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
           'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
           'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
           'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
           'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
           'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'aq_cid10', 'aq_linfin', 'aq_estadi',
           'aq_grahis', 'aq_dtiden', 'aq_trante', 'aq_cidini1', 'aq_dtini1', 'aq_cidini2', 'aq_dtini2', 'aq_cidini3',
           'aq_dtini3', 'aq_conttr', 'aq_dtintr', 'aq_esqu_p1', 'aq_totmpl', 'aq_totmau', 'aq_esqu_p2', 'aq_med01',
           'aq_med02', 'aq_med03', 'aq_med04', 'aq_med05', 'aq_med06', 'aq_med07', 'aq_med08', 'aq_med09', 'aq_med10',
           'ap_natjur', 'uf', 'ano', 'mes']
        

class ARSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
           'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
           'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
           'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
           'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
           'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'ar_smrd', 'ar_cid10', 'ar_linfin',
           'ar_estadi', 'ar_grahis', 'ar_dtiden', 'ar_trante', 'ar_cidini1', 'ar_dtini1', 'ar_cidini2', 'ar_dtini2',
           'ar_cidini3', 'ar_dtini3', 'ar_conttr', 'ar_dtintr', 'ar_finali', 'ar_cidtr1', 'ar_cidtr2', 'ar_cidtr3',
           'ar_numc1', 'ar_iniar1', 'ar_iniar2', 'ar_iniar3', 'ar_fimar1', 'ar_fimar2', 'ar_fimar3', 'ar_numc2',
           'ar_numc3', 'ap_natjur', 'uf', 'ano', 'mes']
        

class ATDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATDSiasus
        fields = ['ap_mvm', 'ap_condic', 'ap_gestao', 'ap_coduni', 'ap_autoriz', 'ap_cmp', 'ap_pripal', 'ap_vl_ap',
            'ap_ufmun', 'ap_tpups', 'ap_tippre', 'ap_mn_ind', 'ap_cnpjcpf', 'ap_cnpjmnt', 'ap_cnspcn', 'ap_coidade',
            'ap_nuidade', 'ap_sexo', 'ap_racacor', 'ap_munpcn', 'ap_ufnacio', 'ap_ceppcn', 'ap_ufdif', 'ap_mndif',
            'ap_dtinic', 'ap_dtfim', 'ap_tpaten', 'ap_tpapac', 'ap_motsai', 'ap_obito', 'ap_encerr', 'ap_perman',
            'ap_alta', 'ap_transf', 'ap_dtocor', 'ap_codemi', 'ap_catend', 'ap_apacant', 'ap_unisol', 'ap_dtsolic',
            'ap_dtaut', 'ap_cidcas', 'ap_cidpri', 'ap_cidsec', 'ap_etnia', 'atd_caract', 'atd_dtpdr', 'atd_dtcli',
            'atd_acevas', 'atd_maisne', 'atd_sitini', 'atd_sittra', 'atd_seapto', 'atd_hb', 'atd_fosfor', 'atd_ktvsem',
            'atd_tru', 'atd_albumi', 'atd_pth', 'atd_hiv', 'atd_hcv', 'atd_hbsag', 'atd_interc', 'atd_seperi', 'ap_natjur']


class PASerializer(serializers.ModelSerializer):
    class Meta:
        model = PASiasus
        fields = ['pa_coduni', 'pa_gestao', 'pa_condic', 'pa_ufmun', 'pa_regct', 'pa_incout', 'pa_incurg', 'pa_tpups',
                  'pa_tippre', 'pa_mn_ind', 'pa_cnpjcpf', 'pa_cnpjmnt', 'pa_cnpj_cc', 'pa_mvm', 'pa_cmp', 'pa_proc_id',
                  'pa_tpfin', 'pa_subfin', 'pa_nivcpl', 'pa_docorig', 'pa_autoriz', 'pa_cnsmed', 'pa_cbocod', 'pa_motsai',
                  'pa_obito', 'pa_encerr', 'pa_perman', 'pa_alta', 'pa_transf', 'pa_cidpri', 'pa_cidsec', 'pa_cidcas',
                  'pa_catend', 'pa_idade', 'idademin', 'idademax', 'pa_flidade', 'pa_sexo', 'pa_racacor', 'pa_munpcn',
                  'pa_qtdpro', 'pa_qtdapr', 'pa_valpro', 'pa_valapr', 'pa_ufdif', 'pa_mndif', 'pa_dif_val', 'nu_vpa_tot',
                  'nu_pa_tot', 'pa_indica', 'pa_codoco', 'pa_flqt', 'pa_fler', 'pa_etnia', 'pa_vl_cf', 'pa_vl_cl',
                  'pa_vl_inc', 'pa_srv_c', 'pa_ine', 'pa_nat_jur', 'uf', 'ano', 'mes']