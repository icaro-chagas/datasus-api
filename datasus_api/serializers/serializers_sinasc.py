from rest_framework import serializers
from ..models.sinasc.dn import DNSinasc
from ..models.sinasc.dnex import DNEXSinasc


class DNSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSinasc
        fields = ['origem', 'codestab', 'codmunnasc', 'locnasc', 'idademae', 'estcivmae', 'escmae', 'codocupmae',
                  'qtdfilvivo', 'qtdfilmort', 'codmunres', 'gestacao', 'gravidez', 'parto', 'consultas', 'dtnasc',
                  'horanasc', 'sexo', 'apgar1', 'apgar5', 'racacor', 'peso', 'idanomal', 'dtcadastro', 'codanomal',
                  'numerolote', 'versaosist', 'dtrecebim', 'difdata', 'dtrecoriga', 'naturalmae', 'codmunnatu',
                  'codufnatu', 'escmae2010', 'seriescmae', 'dtnascmae', 'racacormae', 'qtdgestant', 'qtdpartnor',
                  'qtdpartces', 'idadepai', 'dtultmenst', 'semagestac', 'tpmetestim', 'consprenat', 'mesprenat',
                  'tpapresent', 'sttrabpart', 'stcesparto', 'tpnascassi', 'tpfuncresp', 'tpdocresp', 'dtdeclarac',
                  'escmaeagr1', 'stdnepidem', 'stdnnova', 'codpaisres', 'tprobson', 'paridade', 'kotelchuck', 'contador']


class DNEXSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNEXSinasc
        fields = ['origem', 'codestab', 'codmunnasc', 'locnasc', 'idademae', 'estcivmae', 'escmae', 'codocupmae',
                  'qtdfilvivo', 'qtdfilmort', 'codmunres', 'gestacao', 'gravidez', 'parto', 'consultas', 'dtnasc',
                  'horanasc', 'sexo', 'apgar1', 'apgar5', 'racacor', 'peso', 'idanomal', 'dtcadastro', 'codanomal',
                  'numerolote', 'versaosist', 'dtrecebim', 'difdata', 'dtrecoriga', 'naturalmae', 'codmunnatu',
                  'codufnatu', 'escmae2010', 'seriescmae', 'dtnascmae', 'racacormae', 'qtdgestant', 'qtdpartnor',
                  'qtdpartces', 'idadepai', 'dtultmenst', 'semagestac', 'tpmetestim', 'consprenat', 'mesprenat',
                  'tpapresent', 'sttrabpart', 'stcesparto', 'tpnascassi', 'tpfuncresp', 'tpdocresp', 'dtdeclarac',
                  'escmaeagr1', 'stdnepidem', 'stdnnova', 'codpaisres', 'tprobson', 'paridade', 'kotelchuck', 'contador']