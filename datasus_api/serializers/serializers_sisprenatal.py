from rest_framework import serializers
from ..models.sisprenatal.pn import PNSisprenatal


class PNSerializer(serializers.ModelSerializer):
    class Meta:
        model = PNSisprenatal
        fields = ['nu_ano_ges', 'dt_atend', 'co_uf_ibge', 'nu_gesta', 'co_gestant', 'co_pais', 'nu_cns',
                  'nu_idade', 'nu_nis', 'nu_nis_rep', 'ds_zona', 'qt_ab_ect', 'qt_ab_ger', 'qt_ab_mol',
                  'qt_mor_aps', 'qt_mor_ps', 'qt_nsc_mor', 'qt_nsc_viv', 'qt_prt_cir', 'qt_prt_for',
                  'qt_prt_vag', 'st_aux_dsl', 'st_gra_ant', 'st_gra_pla', 'dt_dum', 'dt_dpp', 'co_tpo_gra',
                  'co_esc_gp', 'co_rac_gp', 'co_etn_gp', 'co_stf_gp', 'co_mun_ubs', 'qt_cons', 'qt_consult',
                  'st_gestac', 'dt_inc', 'uf', 'ano', 'mes']
        


