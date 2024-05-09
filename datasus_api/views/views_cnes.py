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
from ..models.file_metadata import FileMetadata
from ..serializers.serializers_cnes import DCSerializer, EESerializer, EFSerializer, EPSerializer, EQSerializer
from ..serializers.serializers_cnes import GMSerializer, HBSerializer, INSerializer, LTSerializer, PFSerializer
from ..serializers.serializers_cnes import RCSerializer, SRSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..util.postgresql_util import PostgresDbOperations
from ..util.datasus_util import download_file
from drf_yasg.utils import swagger_auto_schema
from ..util.doc_api_util import uf_param_post, month_param_post, year_param_post
from ..util.doc_api_util import uf_param_delete, month_param_delete, year_param_delete
from ..util.doc_api_util import uf_param_get, month_param_get, year_param_get, page_number_get

MAX_ROWS_PER_PAGE = 200000
BASE_NAME = 'CNES'

TABLE_NAMES = {
    'DC': 'dc_cnes',
    'EE': 'ee_cnes',
    'EF': 'ef_cnes',
    'EP': 'ep_cnes',
    'EQ': 'eq_cnes',
    'GM': 'gm_cnes',
    'HB': 'hb_cnes',
    'IN': 'in_cnes',
    'LT': 'lt_cnes',
    'PF': 'pf_cnes',
    'RC': 'rc_cnes',
    'SR': 'sr_cnes'
}

MODELS = {
    'DC': DCCnes,
    'EE': EECnes,
    'EF': EFCnes,
    'EP': EPCnes,
    'EQ': EQCnes,
    'GM': GMCnes,
    'HB': HBCnes,
    'IN': INCnes,
    'LT': LTCnes,
    'PF': PFCnes,
    'RC': RCCnes,
    'SR': SRCnes
}

SERIALIZERS = {
    'DC': DCSerializer,
    'EE': EESerializer,
    'EF': EFSerializer,
    'EP': EPSerializer,
    'EQ': EQSerializer,
    'GM': GMSerializer,
    'HB': HBSerializer,
    'IN': INSerializer,
    'LT': LTSerializer,
    'PF': PFSerializer,
    'RC': RCSerializer,
    'SR': SRSerializer
}

@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do EE', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/EE']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do EE', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/EE']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do EE', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/EE'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ee(request, format='json'):
    return handle_request(request, 'EE')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DC', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/DC']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DC', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/DC']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DC', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/DC'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_dc(request):
    return handle_request(request, 'DC')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do EF', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/EF']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do EF', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/EF']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do EF', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/EF'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ef(request):
    return handle_request(request, 'EF')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do EP', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/EP']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do EP', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/EP']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do EP', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/EP'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ep(request):
    return handle_request(request, 'EP')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do EQ', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/EQ']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do EQ', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/EQ']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do EQ', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/EQ'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_eq(request):
    return handle_request(request, 'EQ')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do GM', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/GM']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do GM', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/GM']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do GM', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/GM'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_gm(request):
    return handle_request(request, 'GM')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do HB', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/HB']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do HB', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/HB']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do HB', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/HB'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_hb(request):
    return handle_request(request, 'HB')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do IN', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/IN']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do IN', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/IN']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do IN', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/IN'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_in(request):
    return handle_request(request, 'IN')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do LT', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/LT']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do LT', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/LT']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do LT', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/LT'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_lt(request):
    return handle_request(request, 'LT')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do PF', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/PF']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do PF', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/PF']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do PF', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/PF'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_pf(request):
    return handle_request(request, 'PF')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do RC', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/RC']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do RC', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/RC']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do RC', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/RC'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_rc(request):
    return handle_request(request, 'RC')


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do SR', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['CNES/SR']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do SR', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['CNES/SR']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do SR', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['CNES/SR'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_sr(request):
    return handle_request(request, 'SR')


def handle_request(request, prefix):
    if request.method == 'GET':
        return get(request, prefix)
    elif request.method == 'POST':
        return insert(request, prefix)
    elif request.method == 'DELETE':
        return delete(request, prefix)


def insert(request, prefix):
    uf = request.GET.get('uf')
    month = request.GET.get('month')
    full_year = request.GET.get('year')

    if any(map(lambda x: x is None, [uf, full_year, month])):
        return Response({'message': 'The uf, month and year parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    uf = uf.upper()
    year = full_year[2:]
    if len(month) == 1:
        month = f'0{month}'

    filename = f'{prefix}{uf}{year}{month}'

    dbo = PostgresDbOperations(TABLE_NAMES[prefix])
    inserted_files = dbo.get_inserted_files()
    if filename in inserted_files:
        return Response({'message': f'The {filename} file has already been inserted'}, status=status.HTTP_409_CONFLICT)
    
    try:
        download_file('CNES', filename, prefix)
        dbo.insert_file(filename, prefix, uf, full_year, month)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_201_CREATED)


def get(request, prefix):

    uf = request.GET.get('uf')
    year = request.GET.get('year')
    month = request.GET.get('month')
    page_number = request.GET.get('page', 1)

    if uf:
        uf = uf.upper()
    if month and len(month) == 1:
        month = f'0{month}'

    return Response(get_aux(prefix, uf, month, year, page_number))


def get_aux(prefix, uf, month, year, page_number):
    offset = (page_number - 1) * MAX_ROWS_PER_PAGE
    limit = MAX_ROWS_PER_PAGE

    data = None
    objs = None
    model = MODELS[prefix]
    if all([uf, month, year]):
        objs = model.objects.filter(uf=uf, mes=month, ano=year).order_by('id')[offset:offset + limit]

    elif all([uf, year]):
        objs = model.objects.filter(uf=uf, ano=year).order_by('id')[offset:offset + limit]

    elif all([uf, month]):
        objs = model.objects.filter(uf=uf, mes=month).order_by('id')[offset:offset + limit]

    elif all([year, month]):
        objs = model.objects.filter(ano=year, mes=month).order_by('id')[offset:offset + limit]

    elif uf:
        objs = model.objects.filter(uf=uf).order_by('id')[offset:offset + limit]
    
    elif month:
        objs = model.objects.filter(mes=month).order_by('id')[offset:offset + limit]

    elif year:
        objs = model.objects.filter(ano=year).order_by('id')[offset:offset + limit]

    else:
        objs = model.objects.all().order_by('id')[offset:offset + limit]

    if objs:
        serializer = SERIALIZERS[prefix]

        data = serializer(objs, many=True).data

    return data


def delete(request, prefix):
    uf = request.GET.get('uf')
    year = request.GET.get('year')
    month = request.GET.get('month')

    if uf is None:
        return Response({'message': 'The uf parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    uf = uf.upper()
    if month and len(month) == 1:
        month = f'0{month}'

    delete_aux(prefix, uf, month, year)

    return Response(status=status.HTTP_204_NO_CONTENT)


def delete_aux(prefix, uf, month, year):

    model = MODELS[prefix]
    if all([uf, month, year]):
        model.objects.filter(uf=uf, mes=month, ano=year).delete()
        FileMetadata.objects.filter(prefix=prefix, uf=uf, month=month, year=year).delete()
    
    elif all([uf, year]):
        model.objects.filter(uf=uf, ano=year).delete()
        FileMetadata.objects.filter(prefix=prefix, uf=uf, year=year).delete()


    elif all([uf, month]):
        model.objects.filter(uf=uf, mes=month).delete()
        FileMetadata.objects.filter(prefix=prefix, uf=uf, month=month).delete()
    
    elif uf:
        model.objects.filter(uf=uf).delete()
        FileMetadata.objects.filter(prefix=prefix, uf=uf).delete()