from rest_framework import serializers
from ..models.cnes.dc import DCCnes
from ..models.cnes.ee import EECnes
from ..models.cnes.ef import EFCnes
from ..models.cnes.ep import EPCnes
from ..models.cnes.eq import EQCnes
from ..models.cnes.gm import GMCnes
from ..models.cnes.hb import HBCnes
from ..models.cnes.inc import INCnes
from ..models.cnes.lt import LTCnes
from ..models.cnes.pf import PFCnes
from ..models.cnes.rc import RCCnes
from ..models.cnes.sr import SRCnes


class DCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DCCnes
        fields = ['cnes', 'codufmun', 'cpf_cnpj', 'pf_pj', 'niv_dep', 'cnpj_man', 'cod_ir', 'regsaude', 'micr_reg',
                  'distrsan', 'vinc_sus', 'distradm', 'tpgestao', 'esfera_a', 'retencao', 'atividad', 'natureza',
                  'clientel', 'tp_unid', 'turno_at', 'niv_hier', 'tp_prest', 's_hbsagp', 's_hbsagn', 's_dpi', 's_dpac',
                  's_reagp', 's_reagn', 's_rehcv', 'maq_prop', 'maq_outr', 'f_areia', 'f_carvao', 'abrandad', 'deioniza',
                  'osmose_r', 'out_trat', 'cns_nefr', 'dialise', 'simul_rd', 'planj_rd', 'armaz_ft', 'conf_mas', 'sala_mol',
                  'blocoper', 's_armaze', 's_prepar', 's_qcdura', 's_qldura', 's_cpflux', 's_simula', 's_acell6', 's_alseme',
                  's_alcome', 'ortv1050', 'orv50150', 'ov150500', 'un_cobal', 'eqbrbaix', 'eqbrmedi', 'eqbralta', 'eq_marea',
                  'eq_mindi', 'eqsispln', 'eqdoscli', 'eqfonsel', 'cns_adm', 'cns_oped', 'cns_conc', 'cns_oclin', 'cns_mrad',
                  'cns_fnuc', 'quimradi', 's_recepc', 's_trihmt', 's_tricli', 's_coleta', 's_aferes', 's_preest', 's_proces',
                  's_estoqu', 's_distri', 's_sorolo', 's_imunoh', 's_pretra', 's_hemost', 's_contrq', 's_biomol', 's_imunfe',
                  's_transf', 's_sgdoad', 'qt_cadre', 'qt_cenre', 'qt_refsa', 'qt_conra', 'qt_extpl', 'qt_fre18', 'qt_fre30',
                  'qt_agipl', 'qt_selad', 'qt_irrhe', 'qt_agltn', 'qt_maqaf', 'qt_refre', 'qt_refas', 'qt_capfl', 'cns_hmtr',
                  'cns_hmtl', 'cns_cres', 'cns_rtec', 'hemotera', 'ap01cv01', 'ap01cv02', 'ap01cv03', 'ap01cv04', 'ap01cv05',
                  'ap01cv06', 'ap01cv07', 'ap02cv01', 'ap02cv02', 'ap02cv03', 'ap02cv04', 'ap02cv05', 'ap02cv06', 'ap02cv07',
                  'ap03cv01', 'ap03cv02', 'ap03cv03', 'ap03cv04', 'ap03cv05', 'ap03cv06', 'ap03cv07', 'ap04cv01', 'ap04cv02',
                  'ap04cv03', 'ap04cv04', 'ap04cv05', 'ap04cv06', 'ap04cv07', 'ap05cv01', 'ap05cv02', 'ap05cv03', 'ap05cv04',
                  'ap05cv05', 'ap05cv06', 'ap05cv07', 'ap06cv01', 'ap06cv02', 'ap06cv03', 'ap06cv04', 'ap06cv05', 'ap06cv06',
                  'ap06cv07', 'ap07cv01', 'ap07cv02', 'ap07cv03', 'ap07cv04', 'ap07cv05', 'ap07cv06', 'ap07cv07', 'atend_pr',
                  'gesprg3e', 'gesprg3m', 'gesprg4e', 'gesprg4m', 'gesprg6e', 'gesprg6m', 'nivate_a', 'nivate_h', 'competen',
                  'nat_jur', 'uf', 'ano', 'mes']


class EESerializer(serializers.ModelSerializer):
    class Meta:
        model = EECnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cod_cep', 'vinc_sus', 'tp_prest', 'sgruphab', 'cmpt_ini', 'cmpt_fim', 'dtportar',
                  'portaria', 'maportar', 'competen', 'nat_jur', 'uf', 'ano', 'mes']
        

class EFSerializer(serializers.ModelSerializer):
    class Meta:
        model = EFCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cod_cep', 'vinc_sus', 'tp_prest', 'sgruphab', 'cmpt_ini', 'cmpt_fim', 'dtportar',
                  'portaria', 'maportar', 'competen', 'nat_jur', 'uf', 'ano', 'mes']


class EPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPCnes
        fields = ['cnes', 'codufmun', 'cod_cep', 'cpf_cnpj', 'pf_pj', 'niv_dep', 'cnpj_man', 'cod_ir', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'vinc_sus',
                 'tpgestao', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at', 'niv_hier', 'terceiro', 'tp_prest', 'gesprg1e',
                 'gesprg1m', 'gesprg2e', 'gesprg2m', 'gesprg4e', 'gesprg4m', 'nivate_a', 'gesprg3e', 'gesprg3m', 'gesprg5e', 'gesprg5m', 'gesprg6e', 'gesprg6m',
                 'nivate_h', 'ap01cv01', 'ap01cv02', 'ap01cv05', 'ap01cv06', 'ap01cv03', 'ap01cv04', 'ap01cv07', 'ap02cv01', 'ap02cv02', 'ap02cv05', 'ap02cv06',
                 'ap02cv03', 'ap02cv04', 'ap02cv07', 'ap03cv01', 'ap03cv02', 'ap03cv05', 'ap03cv06', 'ap03cv03', 'ap03cv04', 'ap03cv07', 'ap04cv01', 'ap04cv02',
                 'ap04cv05', 'ap04cv06', 'ap04cv03', 'ap04cv04', 'ap04cv07', 'ap05cv01', 'ap05cv02', 'ap05cv05', 'ap05cv06', 'ap05cv03', 'ap05cv04', 'ap05cv07',
                 'ap06cv01', 'ap06cv02', 'ap06cv05', 'ap06cv06', 'ap06cv03', 'ap06cv04', 'ap06cv07', 'ap07cv01', 'ap07cv02', 'ap07cv05', 'ap07cv06', 'ap07cv03',
                 'ap07cv04', 'ap07cv07', 'atend_pr', 'idequipe', 'tipo_eqp', 'nome_eqp', 'id_area', 'nomearea', 'id_segm', 'descsegm', 'tiposegm', 'dt_ativa',
                 'dt_desat', 'quilombo', 'assentad', 'popgeral', 'escola', 'indigena', 'pronasci', 'motdesat', 'tp_desat', 'competen', 'nat_jur', 'uf', 'ano', 'mes']
        

class EQSerializer(serializers.ModelSerializer):
    class Meta:
        model = EQCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'atividad', 'retencao', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'tipequip', 'codequip', 'qt_exist', 'qt_uso', 'ind_sus', 'ind_nsus', 'competen',
                  'nat_jur', 'uf', 'ano', 'mes']
        

class GMSerializer(serializers.ModelSerializer):
    class Meta:
        model = GMCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cod_cep', 'vinc_sus', 'tp_prest', 'sgruphab', 'cmpt_ini', 'cmpt_fim', 'dtportar',
                  'portaria', 'maportar', 'competen', 'nat_jur', 'uf', 'ano', 'mes']
        

class HBSerializer(serializers.ModelSerializer):
    class Meta:
        model = HBCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cod_cep', 'vinc_sus', 'tp_prest', 'sgruphab', 'cmpt_ini', 'cmpt_fim',
                  'dtportar', 'portaria', 'maportar', 'nuleitos', 'competen', 'nat_jur', 'uf', 'ano', 'mes']


class INSerializer(serializers.ModelSerializer):
    class Meta:
        model = INCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cod_cep', 'vinc_sus', 'tp_prest', 'sgruphab', 'cmpt_ini', 'cmpt_fim', 'dtportar',
                  'portaria', 'maportar', 'competen', 'nat_jur', 'uf', 'ano', 'mes']


class LTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LTCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'atividad', 'retencao', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'tp_leito', 'codleito', 'qt_exist', 'qt_contr', 'qt_sus', 'qt_nsus', 'competen',
                  'nat_jur', 'uf', 'ano', 'mes']


class PFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PFCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'atividad', 'retencao', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cpf_prof', 'cpfunico', 'cbo', 'cbounico', 'nomeprof', 'cns_prof', 'conselho',
                  'registro', 'vinculac', 'vincul_c', 'vincul_a', 'vincul_n', 'prof_sus', 'profnsus', 'horaoutr',
                  'horahosp', 'hora_amb', 'competen', 'ufmunres', 'nat_jur', 'uf', 'ano', 'mes']
        

class RCSerializer(serializers.ModelSerializer):
    class Meta:
        model = RCCnes
        fields = ['cnes', 'codufmun', 'regsaude', 'micr_reg', 'distrsan', 'distradm', 'tpgestao', 'pf_pj', 'cpf_cnpj',
                  'niv_dep', 'cnpj_man', 'esfera_a', 'retencao', 'atividad', 'natureza', 'clientel', 'tp_unid', 'turno_at',
                  'niv_hier', 'terceiro', 'cod_cep', 'vinc_sus', 'tp_prest', 'sgruphab', 'cmpt_ini', 'cmpt_fim', 'dtportar',
                  'portaria', 'maportar', 'competen', 'nat_jur', 'uf', 'ano', 'mes']
        
        
class SRSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRCnes
        fields = ['cnes', 'codufmun', 'serv_esp', 'class_sr', 'srvunico', 'regsaude', 'micr_reg', 'distrsan', 'distradm',
                  'tpgestao', 'pf_pj', 'cpf_cnpj', 'niv_dep', 'esfera_a', 'atividad', 'retencao', 'natureza', 'clientel',
                  'tp_unid', 'turno_at', 'niv_hier', 'terceiro', 'cnpj_man', 'caracter', 'amb_nsus', 'amb_sus', 'hosp_nsus',
                  'hosp_sus', 'competen', 'contsrvu', 'cnesterc', 'nat_jur'] 

