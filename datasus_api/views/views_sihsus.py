from ..models.sihsus.er import ERSihsus
from ..models.sihsus.rd import RDSihsus
from ..models.sihsus.rj import RJSihsus
from ..models.sihsus.sp import SPSihsus
from ..models.file_metadata import FileMetadata
from ..serializers.serializers_sihsus import ERSerializer, RDSerializer, RJSerializer, SPSializer
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

TABLE_NAMES = {
    'ER': 'er_sihsus',
    'RD': 'rd_sihsus',
    'RJ': 'rj_sihsus',
    'SP': 'sp_sihsus',
}

MODELS = {
    'ER': ERSihsus,
    'RD': RDSihsus,
    'RJ': RJSihsus,
    'SP': SPSihsus,
}

SERIALIZERS = {
    'ER': ERSerializer,
    'RD': RDSerializer,
    'RJ': RJSerializer,
    'SP': SPSializer,
}


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do ER', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIHSUS/ER']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do ER', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIHSUS/ER']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do ER', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIHSUS/ER'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_er(request, format=None):
    return handle_request(request, 'ER', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do RD', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIHSUS/RD']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do RD', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIHSUS/RD']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do RD', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIHSUS/RD'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_rd(request, format=None):
    return handle_request(request, 'RD', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do RJ', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIHSUS/RJ']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do RJ', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIHSUS/RJ']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do RJ', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIHSUS/RJ'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_rj(request, format=None):
    return handle_request(request, 'RJ', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do SP', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, month_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIHSUS/SP']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do SP', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, month_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIHSUS/SP']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do SP', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, month_param_delete, year_param_delete], tags=['SIHSUS/SP'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_sp(request, format=None):
    return handle_request(request, 'SP', format)


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
        base_name = 'SIHSUS1'
    else:
        base_name = 'SIHSUS2'

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