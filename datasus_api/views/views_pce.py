from ..models.pce.pce import PCE
from ..models.file_metadata import FileMetadata
from ..serializers.serializers_pce import PCESerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..util.postgresql_util import PostgresDbOperations
from ..util.datasus_util import download_file
from drf_yasg.utils import swagger_auto_schema
from ..util.doc_api_util import uf_param_post, year_param_post
from ..util.doc_api_util import uf_param_delete, year_param_delete
from ..util.doc_api_util import uf_param_get, year_param_get, page_number_get


MAX_ROWS_PER_PAGE = 200000
BASE_NAME = 'PCE'

TABLE_NAMES = {
    'PCE': 'pce'
}

MODELS = {
    'PCE': PCE
}

SERIALIZERS = {
    'PCE': PCESerializer
}


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do PCE', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['PCE']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do PCE', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['PCE']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do PCE', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, year_param_delete], tags=['PCE'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_pce(request, format=None):
    return handle_request(request, 'PCE', format)


def handle_request(request, prefix, format=None):
    if request.method == 'GET':
        return get(request, prefix, format)
    elif request.method == 'POST':
        return insert(request, prefix, format)
    elif request.method == 'DELETE':
        return delete(request, prefix, format)


def insert(request, prefix, format=None):
    uf = request.GET.get('uf')
    full_year = request.GET.get('year')

    if any(map(lambda x: x is None, [uf, full_year])):
        return Response({'message': 'The uf and year parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    uf = uf.upper()
    year = full_year[2:]

    filename = f'{prefix}{uf}{year}'

    dbo = PostgresDbOperations(TABLE_NAMES[prefix])
    inserted_files = dbo.get_inserted_files()
    if filename in inserted_files:
        return Response({'message': f'The {filename} file has already been inserted'}, status=status.HTTP_409_CONFLICT)
    
    try:
        download_file(BASE_NAME, filename, prefix)
        dbo.insert_file(filename, prefix, uf, full_year)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_201_CREATED)


def get(request, prefix, format=None):

    uf = request.GET.get('uf')
    year = request.GET.get('year')
    page_number = request.GET.get('page', 1)

    if uf:
        uf = uf.upper()

    return Response(get_aux(prefix, uf, year, page_number))


def get_aux(prefix, uf, year, page_number):
    offset = (page_number - 1) * MAX_ROWS_PER_PAGE
    limit = MAX_ROWS_PER_PAGE

    data = None
    objs = None
    model = MODELS[prefix]

    if all([uf, year]):
        objs = model.objects.filter(uf=uf, ano=year).order_by('id')[offset:offset + limit]

    elif uf:
        objs = model.objects.filter(uf=uf).order_by('id')[offset:offset + limit]

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

    if uf is None:
        return Response({'message': 'The uf parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    uf = uf.upper()

    delete_aux(prefix, uf, year)

    return Response(status=status.HTTP_204_NO_CONTENT)


def delete_aux(prefix, uf, year):

    model = MODELS[prefix]
    
    if all([uf, year]):
        model.objects.filter(uf=uf, ano=year).delete()
        FileMetadata.objects.filter(prefix=prefix, uf=uf, year=year).delete()
    
    elif uf:
        model.objects.filter(uf=uf).delete()
        FileMetadata.objects.filter(prefix=prefix, uf=uf).delete()