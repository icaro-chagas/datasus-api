from rest_framework import serializers
from ..models.siasus.pa import PASiasus


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