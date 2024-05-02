from rest_framework import serializers
from ..models.sismama.cm import CMSismama
from ..models.sismama.hm import HMSismama


class CMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSismama
        fields = ['co_pac_uf', 'co_us_uf', 'co_pac_ibg', 'co_us_ibge', 'co_us', 'co_cnes', 'prestuf',
                  'regus', 'regresid', 'reglab', 'ano_comp', 'prestmun', 'dt_id_comp', 'co_fx_etar',
                  'co_pac_esc', 'co_pac_sex', 'co_pac_rac', 'canmpacanc', 'co_cli_des', 'co_cli_nod',
                  'cclimatmam', 'cclimatdpc', 'dintcoleta', 'dintresult', 'dinttempex', 'co_res_ade',
                  'presulpaaf', 'cresbenig', 'cresmaliin', 'cressusmal', 'cresposmal', 'cresderpap',
                  'quantexame', 'pbenmastit', 'pbenabsuba', 'pbenfibroa', 'pbennecgor', 'pbencondfi',
                  'pbenlesepi', 'pbenoutras', 'pmalintump', 'pmalintumf', 'pmalinoutr', 'psuslejpca',
                  'psusoutros', 'pposmacduc', 'pposmaclob', 'pposmacout', 'dematacelu', 'denegmalig',
                  'demaliindt', 'deposmalig', 'delesmalig', 'deprocinfl', 'uf', 'ano', 'mes']


class HMSerializer(serializers.ModelSerializer):
    class Meta:
        model = HMSismama
        fields = ['co_pac_uf', 'co_us_uf', 'co_pac_ibg', 'co_us_ibge', 'co_us', 'co_cnes', 'prestuf',
                  'prestmun', 'regus', 'regresid', 'reglab', 'ano_comp', 'dt_id_comp', 'co_fx_etar',
                  'co_pac_esc', 'co_pac_sex', 'co_pac_rac', 'cclitpexa', 'cclitant', 'cclidiagim',
                  'ccliloca', 'chislinfco', 'chisreces', 'chisrecpr', 'c_cli_tcan', 'c_cli_dete',
                  'co_cli_mam', 'co_cli_tam', 'co_tam_tum', 'c_cli_linf', 'cclimatpro', 'dintcoleta',
                  'dintresult', 'dinttempex', 'cresprocir', 'co_res_ade', 'cmicmicrca', 'c_neo_mali',
                  'co_his_gra', 'co_his_mar', 'quantexame', 'lesbenigin', 'cneomalig', 'cbenhipsat',
                  'cbenhipcat', 'cbenlobcat', 'cbenadenos', 'cbenesdero', 'cbenfibroc', 'cbenfibroa',
                  'cbensolita', 'cbenmulti', 'cbenflorid', 'cbenmastit', 'cbenoutros', 'uf', 'ano', 'mes']
        


