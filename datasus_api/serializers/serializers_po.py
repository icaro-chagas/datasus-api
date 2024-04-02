from rest_framework import serializers
from ..models.po.po import PO


class POSerializer(serializers.ModelSerializer):
    class Meta:
        model = PO
        fields = ['ano_diagn', 'anomes_dia', 'ano_tratam', 'anomes_tra', 'uf_resid', 'mun_resid', 'uf_tratam', 'mun_tratam',
                  'uf_diagn', 'mun_diag', 'tratamento', 'diagnostic', 'idade', 'sexo', 'estadiam', 'cnes_diag', 'cnes_trat',
                  'tempo_trat', 'cns_pac', 'diag_deth', 'dt_diag', 'dt_trat', 'dt_nasc', 'uf', 'ano']

