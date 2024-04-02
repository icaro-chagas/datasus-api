from rest_framework import serializers
from ..models.pce.pce import PCE


class PCESerializer(serializers.ModelSerializer):
    class Meta:
        model = PCE
        fields = ['id_uf', 'sg_uf', 'id_distr', 'id_loc', 'dt_comp', 'qt_pop', 'qt_pred', 'qt_exam', 'qt_nrecol', 'qt_1a4',
                  'qt_5a16', 'qt_17', 'qt_pos', 'qt_atrat', 'qt_trat', 'qt_ci', 'qt_rec', 'qt_aus', 'qt_asc', 'qt_anc',
                  'qt_tae', 'qt_tt', 'qt_ev', 'qt_se', 'qt_hn', 'qt_out', 'qt_cap', 'qt_pesq', 'qt_bgla', 'qt_bstr',
                  'qt_bten', 'qt_out1', 'qt_posbgla', 'qt_posbten', 'qt_posbstr', 'qt_posout', 'uf', 'ano']

