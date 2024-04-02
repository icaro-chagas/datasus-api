from rest_framework import serializers
from ..models.ciha.ciha import CIHA


class CIHASerializer(serializers.ModelSerializer):
    class Meta:
        model = CIHA
        fields = ['ano_cmpt', 'mes_cmpt', 'espec', 'cgc_hosp', 'munic_res', 'nasc', 'sexo', 'uti_mes_to', 'uti_int_to',
                  'proc_rea', 'qt_proc', 'dt_atend', 'dt_saida', 'diag_princ', 'diag_secun', 'cobranca', 'natureza',
                  'gestao', 'munic_mov', 'cod_idade', 'idade', 'dias_perm', 'morte', 'nacional', 'car_int', 'homonimo',
                  'cnes', 'fonte', 'modalidade', 'uf', 'ano', 'mes']

