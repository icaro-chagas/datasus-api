from ..models.siasus.ab import ABSiasus
from ..models.siasus.abo import ABOSiasus
from ..models.siasus.acf import ACFSiasus
from ..models.siasus.ad import ADSiasus
from ..models.siasus.am import AMSiasus
from ..models.siasus.an import ANSiasus
from ..models.siasus.aq import AQSiasus
from ..models.siasus.ar import ARSiasus
from ..models.siasus.atd import ATDSiasus
from ..models.siasus.pa import PASiasus
from ..models.siasus.ps import PSSiasus
from ..models.siasus.sad import SADSiasus
from ..models.file_metadata import FileMetadata
from ..serializers.serializers_siasus import ABSerializer, ABOSerializer, ACFSerializer, ADSerializer, AMSerializer
from ..serializers.serializers_siasus import ANSerializer, AQSerializer, ARSerializer, ATDSerializer, PASerializer
from ..serializers.serializers_siasus import PSSerializer, SADSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..util.postgresql_util import PostgresDbOperations
from ..util.datasus_util import download_file
from drf_yasg.utils import swagger_auto_schema
from ..util.doc_api_util import uf_param_delete, month_param_delete, year_param_delete
from ..util.doc_api_util import uf_param_get, month_param_get, year_param_get, page_number_get
from ..util.doc_api_util import uf_param_post, month_param_post, year_param_post, letter_param_post, letter_param_post


MAX_ROWS_PER_PAGE = 200000

TABLE_NAMES = {
    'AB': 'ab_siasus',
    'ABO': 'abo_siasus',
    'ACF': 'acf_siasus',
    'AD': 'ad_siasus',
    'AM': 'am_siasus',
    'AN': 'an_siasus',
    'AQ': 'aq_siasus',
    'AR': 'ar_siasus',
    'ATD': 'atd_siasus',
    'PA': 'pa_siasus',
    'PS': 'ps_siasus',
    'SAD': 'sad_siasus'

}

MODELS = {
    'AB': ABSiasus,
    'ABO': ABOSiasus,
    'ACF': ACFSiasus,
    'AD': ADSiasus,
    'AM': AMSiasus,
    'AN': ANSiasus,
    'AQ': AQSiasus,
    'AR': ARSiasus,
    'ATD': ATDSiasus,
    'PA': PASiasus,
    'PS': PSSiasus,
    'SAD': SADSiasus
}

SERIALIZERS = {
    'AB': ABSerializer,
    'ABO': ABOSerializer,
    'ACF': ACFSerializer,
    'AD': ADSerializer,
    'AM': AMSerializer,
    'AN': ANSerializer,
    'AQ': AQSerializer,
    'AR': ARSerializer,
    'ATD': ATDSerializer,
    'PA': PASerializer,
    'PS': PSSerializer,
    'SAD': SADSerializer
}


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do AB', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/AB']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do AB', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/AB']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do AB', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/AB'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ab(request, format=None):
    return handle_request(request, 'AB', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do ABO', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/ABO']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do ABO', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/ABO']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do ABO', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/ABO'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_abo(request, format=None):
    return handle_request(request, 'ABO', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do ACF', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/ACF']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do ACF', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/ACF']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do ACF', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/ACF'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_acf(request, format=None):
    return handle_request(request, 'ACF', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do AD', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/AD']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do AD', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/AD']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do AD', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/AD'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ad(request, format=None):
    return handle_request(request, 'AD', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do AM', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/AM']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do AM', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/AM']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do AM', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/AM'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_am(request, format=None):
    return handle_request(request, 'AM', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do AN', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/AN']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do AN', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/AN']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do AN', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/AN'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_an(request, format=None):
    return handle_request(request, 'AN', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do AQ', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/AQ']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do AQ', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/AQ']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do AQ', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/AQ'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_aq(request, format=None):
    return handle_request(request, 'AQ', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do AR', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/AR']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do AR', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/AR']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do AR', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/AR'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ar(request, format=None):
    return handle_request(request, 'AR', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do ATD', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/ATD']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do ATD', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/ATD']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do ATD', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/ATD'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_atd(request, format=None):
    return handle_request(request, 'ATD', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do PA', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/PA']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do PA', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/PA']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do PA', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/PA'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_pa(request, format=None):
    return handle_request(request, 'PA', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do PS', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/PS']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do PS', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/PS']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do PS', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/PS'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ps(request, format=None):
    return handle_request(request, 'PS', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do SAD', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIASUS/SAD']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do SAD', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post, letter_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIASUS/SAD']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do SAD', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIASUS/SAD'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_sad(request, format=None):
    return handle_request(request, 'SAD', format)


def handle_request(request, prefix, format=None):
    if request.method == 'GET':
        return get(request, prefix, format)
    elif request.method == 'POST':
        return insert(request, prefix, format)
    elif request.method == 'DELETE':
        return delete(request, prefix, format)


def insert(request, prefix, format=None):
    uf = request.GET.get('uf')
    month = request.GET.get('month')
    full_year = request.GET.get('year')
    letter = request.GET.get('letter', '')

    if any(map(lambda x: x is None, [uf, full_year, month])):
        return Response({'message': 'The uf, month and year parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    uf = uf.upper()
    year = full_year[2:]
    if len(month) == 1:
        month = f'0{month}'

    filename = f'{prefix}{uf}{year}{month}{letter}'

    dbo = PostgresDbOperations(TABLE_NAMES[prefix])
    inserted_files = dbo.get_inserted_files()
    if filename in inserted_files:
        return Response({'message': f'The {filename} file has already been inserted'}, status=status.HTTP_409_CONFLICT)
    
    if int(full_year) > 2007:
        base_name = 'SIASUS1'
    else:
        base_name = 'SIASUS2'

    try:
        download_file(base_name, filename, prefix)
        dbo.insert_file(filename, prefix, uf, full_year, month)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_201_CREATED)


def get(request, prefix, format=None):

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


def delete(request, prefix, format=None):
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