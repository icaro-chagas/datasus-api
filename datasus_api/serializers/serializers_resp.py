from rest_framework import serializers
from ..models.resp.resp import RESP


class RESPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RESP
        fields = ['co_seq', 'dt_notific', 'ano_not', 'tp_notific', 'dt_nascmae', 'idadeges', 'racacor', 'regiaores',
                  'ufres', 'codmunres', 'sexo', 'dt_nasc', 'ano_nasc', 'peso', 'compriment', 'perimcefal', 'diamcefal',
                  'microcefal', 'def_neuro', 'def_audit', 'def_visual', 'tpdeteccao', 'gest_diag', 'gravidez', 'class_feto',
                  'dt_sintoma', 'febre_ges', 'exant_ges', 'prurido', 'conjuntiv', 'dor_artic', 'dor_musc', 'edema', 'cefaleia',
                  'hipert_gan', 'neurolog', 'exa_torsch', 'resul_s', 'resul_to', 'resul_c', 'resul_h', 'resul_z', 'so_igg_z',
                  'so_igm_z', 'tr_igg_z', 'tr_igm_z', 'pcr_z', 'hist_arbov', 'hist_malfo', 'rnexa_tors', 'rnresul_s', 'rnresul_to',
                  'rnresul_c', 'rnresul_h', 'rnresul_z', 'rnso_igg_z', 'rnso_igm_z', 'rntr_igg_z', 'rntr_igm_z', 'rnpcr_z',
                  'exame_uss', 'dt_uss', 'exa_transf', 'dt_transf', 'exame_tc', 'dt_tc', 'exame_rs', 'dt_rs', 'regiaonot', 'ufnot',
                  'codmunnot', 'st_obito', 'dt_obito', 'classifin', 'etiologia', 'criterio', 'status_not', 'dt_ult_alt', 'uf', 'ano']

