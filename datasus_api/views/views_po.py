from ..models.po.po import PO
from ..models.file_metadata import FileMetadata
from ..serializers.serializers_po import POSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..util.postgresql_util import PostgresDbOperations
from ..util.datasus_util import download_file
from drf_yasg.utils import swagger_auto_schema
from ..util.doc_api_util import month_param_get, year_param_get
from ..util.doc_api_util import month_param_post, year_param_post
from ..util.doc_api_util import month_param_delete, year_param_delete


MAX_ROWS_PER_PAGE = 200000
BASE_NAME = 'PO'

TABLE_NAMES = {
    'PO': 'po'
}

MODELS = {
    'PO': PO
}

SERIALIZERS = {
    'PO': POSerializer
}

@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do PO', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters= [year_param_get], responses={200: 'OK'}, tags=['PO']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do PO', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters= [year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['PO']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do PO', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters= [year_param_delete], tags=['PO'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_po(request, format=None):
    return handle_request(request, 'PO', format)


def handle_request(request, prefix, format=None):
    if request.method == 'GET':
        return get(request, prefix, format)
    elif request.method == 'POST':
        return insert(request, prefix, format)
    elif request.method == 'DELETE':
        return delete(request, prefix, format)


def insert(request, prefix, format=None):
    year = request.GET.get('year')

    if not year:
        return Response({'message': 'The year parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    uf = 'BR'

    filename = f'{prefix}{uf}{year}'

    dbo = PostgresDbOperations(TABLE_NAMES[prefix])
    inserted_files = dbo.get_inserted_files()
    if filename in inserted_files:
        return Response({'message': f'The {filename} file has already been inserted'}, status=status.HTTP_409_CONFLICT)
    
    try:
        download_file(BASE_NAME, filename, prefix)
        dbo.insert_file(filename, prefix, uf, year)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_201_CREATED)


def get(request, prefix, format=None):

    year = request.GET.get('year')
    page_number = request.GET.get('page', 1)

    return Response(get_aux(prefix, year, page_number))


def get_aux(prefix, year, page_number):
    offset = (page_number - 1) * MAX_ROWS_PER_PAGE
    limit = MAX_ROWS_PER_PAGE

    data = None
    objs = None
    model = MODELS[prefix]

    if year:
        objs = model.objects.filter(ano=year).order_by('id')[offset:offset + limit]

    else:
        objs = model.objects.all().order_by('id')[offset:offset + limit]

    if objs:
        serializer = SERIALIZERS[prefix]

        data = serializer(objs, many=True).data

    return data


def delete(request, prefix, format=None):
    year = request.GET.get('year')

    if year is None:
        return Response({'message': 'The year parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    delete_aux(prefix, year)

    return Response(status=status.HTTP_204_NO_CONTENT)


def delete_aux(prefix, year):

    model = MODELS[prefix]
    
    if year:
        model.objects.filter(ano=year).delete()
        FileMetadata.objects.filter(prefix=prefix, year=year).delete()