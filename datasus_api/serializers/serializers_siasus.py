from rest_framework import serializers
from ..models.siasus.pa import PASiasus
from ..models.siasus.ab import ABSiasus


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