from rest_framework import serializers
from ..models.sim.do import DOSim
from ..models.sim.doext import DOEXTSim
from ..models.sim.dofet import DOFETSim
from ..models.sim.doinf import DOINFSim
from ..models.sim.domat import DOMATSim
from ..models.sim.dorext import DOREXTSim


class DOSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOSim
        fields = ['origem', 'tipobito', 'dtobito', 'horaobito', 'natur', 'codmunnatu', 'dtnasc',
           'idade', 'sexo', 'racacor', 'estciv', 'esc', 'esc2010', 'seriescfal', 'ocup',
           'codmunres', 'lococor', 'codestab', 'estabdescr', 'codmunocor', 'idademae', 'escmae',
           'escmae2010', 'seriescmae', 'ocupmae', 'qtdfilvivo', 'qtdfilmort', 'gravidez', 'semagestac',
           'gestacao', 'parto', 'obitoparto', 'peso', 'tpmorteoco', 'obitograv', 'obitopuerp',
           'assistmed', 'exame', 'cirurgia', 'necropsia', 'linhaa', 'linhab', 'linhac', 'linhad',
           'linhaii', 'causabas', 'cb_pre', 'comunsvoim', 'dtatestado', 'circobito', 'acidtrab',
           'fonte', 'numerolote', 'tppos', 'dtinvestig', 'causabas_o', 'dtcadastro', 'atestante',
           'stcodifica', 'codificado', 'versaosist', 'versaoscb', 'fonteinv', 'dtrecebim', 'atestado',
           'dtrecoriga', 'causamat', 'escmaeagr1', 'escfalagr1', 'stdoepidem', 'stdonova', 'difdata',
           'nudiasobco', 'nudiasobin', 'dtcadinv', 'tpobitocor', 'dtconinv', 'fontes', 'tpresginfo',
           'tpnivelinv', 'nudiasinf', 'dtcadinf', 'morteparto', 'dtconcaso', 'fontesinf', 'altcausa',
           'contador', 'uf', 'ano']
        

class DOEXTSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOEXTSim
        fields = ['origem', 'tipobito', 'dtobito', 'horaobito', 'natur', 'codmunnatu', 'dtnasc',
              'idade', 'sexo', 'racacor', 'estciv', 'esc', 'esc2010', 'seriescfal', 'ocup', 
              'codmunres', 'lococor', 'codestab', 'estabdescr', 'codmunocor', 'idademae', 'escmae', 
              'escmae2010', 'seriescmae', 'ocupmae', 'qtdfilvivo', 'qtdfilmort', 'gravidez', 
              'semagestac', 'gestacao', 'parto', 'obitoparto', 'peso', 'tpmorteoco', 'obitograv', 
              'obitopuerp', 'assistmed', 'exame', 'cirurgia', 'necropsia', 'linhaa', 'linhab', 
              'linhac', 'linhad', 'linhaii', 'causabas', 'cb_pre', 'comunsvoim', 'dtatestado', 
              'circobito', 'acidtrab', 'fonte', 'numerolote', 'tppos', 'dtinvestig', 'causabas_o',
              'dtcadastro', 'atestante', 'stcodifica', 'codificado', 'versaosist', 'versaoscb',
              'fonteinv', 'dtrecebim', 'atestado', 'dtrecoriga', 'causamat', 'escmaeagr1',
              'escfalagr1', 'stdoepidem', 'stdonova', 'difdata', 'nudiasobco', 'nudiasobin',
              'dtcadinv', 'tpobitocor', 'dtconinv', 'fontes', 'tpresginfo', 'tpnivelinv',
              'nudiasinf', 'dtcadinf', 'morteparto', 'dtconcaso', 'fontesinf', 'altcausa',
              'contador', 'ano']


class DOFETSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOFETSim
        fields = ['origem', 'codmuncart', 'numregcart', 'codcart', 'dtregcart', 'tipobito', 'dtobito',
              'horaobito', 'natur', 'codmunnatu', 'dtnasc', 'idade', 'sexo', 'racacor', 'estciv',
              'esc', 'esc2010', 'seriescfal', 'ocup', 'codmunres', 'lococor', 'codestab', 'estabdescr',
              'codmunocor', 'idademae', 'escmae', 'escmae2010', 'seriescmae', 'ocupmae', 'qtdfilvivo',
              'qtdfilmort', 'gravidez', 'semagestac', 'gestacao', 'parto', 'obitoparto', 'peso',
              'tpmorteoco', 'obitograv', 'obitopuerp', 'assistmed', 'exame', 'cirurgia', 'necropsia',
              'linhaa', 'linhab', 'linhac', 'linhad', 'linhaii', 'causabas', 'cb_pre', 'medico',
              'comunsvoim', 'dtatestado', 'circobito', 'acidtrab', 'fonte', 'numerolote', 'tppos',
              'dtinvestig', 'linhaa_o', 'linhab_o', 'linhac_o', 'linhad_o', 'linhaii_o', 'causabas_o',
              'dtcadastro', 'atestante', 'stcodifica', 'codificado', 'versaosist', 'versaoscb', 'fonteinv',
              'dtrecebim', 'atestado', 'dtrecorig', 'dtrecoriga', 'causamat', 'escmaeagr1', 'escfalagr1',
              'stdoepidem', 'stdonova', 'difdata', 'nudiasobco', 'nudiasobin', 'dtcadinv', 'tpobitocor',
              'dtconinv', 'fontes', 'tpresginfo', 'tpnivelinv', 'nudiasinf', 'dtcadinf', 'morteparto',
              'dtconcaso', 'fontesinf', 'altcausa', 'contador', 'ano']


class DOINFSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOINFSim
        fields = ['origem', 'tipobito', 'dtobito', 'horaobito', 'natur', 'codmunnatu', 'dtnasc', 'idade', 'sexo',
              'racacor', 'estciv', 'esc', 'esc2010', 'seriescfal', 'ocup', 'codmunres', 'lococor', 'codestab',
              'estabdescr', 'codmunocor', 'idademae', 'escmae', 'escmae2010', 'seriescmae', 'ocupmae',
              'qtdfilvivo', 'qtdfilmort', 'gravidez', 'semagestac', 'gestacao', 'parto', 'obitoparto', 'peso',
              'tpmorteoco', 'obitograv', 'obitopuerp', 'assistmed', 'exame', 'cirurgia', 'necropsia', 'linhaa',
              'linhab', 'linhac', 'linhad', 'linhaii', 'causabas', 'cb_pre', 'comunsvoim', 'dtatestado',
              'circobito', 'acidtrab', 'fonte', 'numerolote', 'tppos', 'dtinvestig', 'causabas_o', 'dtcadastro',
              'atestante', 'stcodifica', 'codificado', 'versaosist', 'versaoscb', 'fonteinv', 'dtrecebim',
              'atestado', 'dtrecoriga', 'causamat', 'escmaeagr1', 'escfalagr1', 'stdoepidem', 'stdonova',
              'difdata', 'nudiasobco', 'nudiasobin', 'dtcadinv', 'tpobitocor', 'dtconinv', 'fontes', 'tpresginfo',
              'tpnivelinv', 'nudiasinf', 'dtcadinf', 'morteparto', 'dtconcaso', 'fontesinf', 'altcausa', 'contador']
        

class DOMATSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOMATSim
        fields = ['origem', 'tipobito', 'dtobito', 'horaobito', 'natur', 'codmunnatu', 'dtnasc', 'idade', 'sexo',
              'racacor', 'estciv', 'esc', 'esc2010', 'seriescfal', 'ocup', 'codmunres', 'lococor', 'codestab',
              'estabdescr', 'codmunocor', 'idademae', 'escmae', 'escmae2010', 'seriescmae', 'ocupmae',
              'qtdfilvivo', 'qtdfilmort', 'gravidez', 'semagestac', 'gestacao', 'parto', 'obitoparto', 'peso',
              'tpmorteoco', 'obitograv', 'obitopuerp', 'assistmed', 'exame', 'cirurgia', 'necropsia', 'linhaa',
              'linhab', 'linhac', 'linhad', 'linhaii', 'causabas', 'cb_pre', 'comunsvoim', 'dtatestado',
              'circobito', 'acidtrab', 'fonte', 'numerolote', 'tppos', 'dtinvestig', 'causabas_o', 'dtcadastro',
              'atestante', 'stcodifica', 'codificado', 'versaosist', 'versaoscb', 'fonteinv', 'dtrecebim',
              'atestado', 'dtrecoriga', 'causamat', 'escmaeagr1', 'escfalagr1', 'stdoepidem', 'stdonova',
              'difdata', 'nudiasobco', 'nudiasobin', 'dtcadinv', 'tpobitocor', 'dtconinv', 'fontes', 'tpresginfo',
              'tpnivelinv', 'nudiasinf', 'dtcadinf', 'morteparto', 'dtconcaso', 'fontesinf', 'altcausa', 'contador']


class DOREXTSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOREXTSim
        fields = ['origem', 'tipobito', 'dtobito', 'horaobito', 'natur', 'codmunnatu', 'dtnasc', 'idade', 'sexo',
               'racacor', 'estciv', 'esc', 'esc2010', 'seriescfal', 'ocup', 'codmunres', 'lococor', 'codestab',
               'estabdescr', 'codmunocor', 'idademae', 'escmae', 'escmae2010', 'seriescmae', 'ocupmae',
               'qtdfilvivo', 'qtdfilmort', 'gravidez', 'semagestac', 'gestacao', 'parto', 'obitoparto', 'peso',
               'tpmorteoco', 'obitograv', 'obitopuerp', 'assistmed', 'exame', 'cirurgia', 'necropsia', 'linhaa',
               'linhab', 'linhac', 'linhad', 'linhaii', 'causabas', 'cb_pre', 'comunsvoim', 'dtatestado',
               'circobito', 'acidtrab', 'fonte', 'numerolote', 'tppos', 'dtinvestig', 'causabas_o', 'dtcadastro',
               'atestante', 'stcodifica', 'codificado', 'versaosist', 'versaoscb', 'fonteinv', 'dtrecebim',
               'atestado', 'dtrecoriga', 'causamat', 'escmaeagr1', 'escfalagr1', 'stdoepidem', 'stdonova',
               'difdata', 'nudiasobco', 'dtcadinv', 'tpobitocor', 'dtconinv', 'fontes', 'tpresginfo', 'tpnivelinv',
               'nudiasinf', 'dtcadinf', 'morteparto', 'dtconcaso', 'fontesinf', 'altcausa', 'contador', 'codpaisres']

