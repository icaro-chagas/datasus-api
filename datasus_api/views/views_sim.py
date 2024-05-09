from ..models.sim.do import DOSim
from ..models.sim.doext import DOEXTSim
from ..models.sim.dofet import DOFETSim
from ..models.sim.doinf import DOINFSim
from ..models.sim.domat import DOMATSim
from ..models.sim.dorext import DOREXTSim
from ..models.file_metadata import FileMetadata
from ..serializers.serializers_sim import DOSerializer, DOEXTSerializer, DOFETSerializer, DOINFSerializer
from ..serializers.serializers_sim import DOMATSerializer, DOREXTSerializer
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
BASE_NAME = 'SIM'

TABLE_NAMES = {
    'DO': 'do_sim',
    'DOEXT': 'doext_sim',
    'DOFET': 'dofet_sim',
    'DOINF': 'doinf_sim',
    'DOMAT': 'domat_sim',
    'DOREXT': 'dorext_sim'
}

MODELS = {
    'DO': DOSim,
    'DOEXT': DOEXTSim,
    'DOFET': DOFETSim,
    'DOINF': DOINFSim,
    'DOMAT': DOMATSim,
    'DOREXT': DOREXTSim
}

SERIALIZERS = {
    'DO': DOSerializer,
    'DOEXT': DOEXTSerializer,
    'DOFET': DOFETSerializer,
    'DOINF': DOINFSerializer,
    'DOMAT': DOMATSerializer,
    'DOREXT': DOREXTSerializer
}


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DO', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_get, year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIM/DO']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DO', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[uf_param_post, year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIM/DO']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DO', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[uf_param_delete, year_param_delete], tags=['SIM/DO'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_do(request, format=None):
    return handle_request(request, 'DO', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DOEXT', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIM/DOEXT']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DOEXT', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIM/DOEXT']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DOEXT', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_delete], tags=['SIM/DOEXT'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_doext(request, format=None):
    return handle_request(request, 'DOEXT', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DOFET', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIM/DOFET']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DOFET', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIM/DOFET']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DOFET', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_delete], tags=['SIM/DOFET'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_dofet(request, format=None):
    return handle_request(request, 'DOFET', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DOINF', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIM/DOINF']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DOINF', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIM/DOINF']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DOINF', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_delete], tags=['SIM/DOINF'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_doinf(request, format=None):
    return handle_request(request, 'DOINF', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DOMAT', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIM/DOMAT']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DOMAT', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIM/DOMAT']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DOMAT', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_delete], tags=['SIM/DOMAT'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_domat(request, format=None):
    return handle_request(request, 'DOMAT', format)


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece dados do DOREXT', operation_description='Fornece dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_get, page_number_get], responses={200: 'OK'}, tags=['SIM/DOREXT']
)
@swagger_auto_schema(
    methods=['POST'], operation_summary='Insere arquivo do DOREXT', operation_description='Baixa e insere os dados de um arquivo do DATASUS no SGBD.',
    manual_parameters=[year_param_post], responses={201: 'Created', 400: 'Bad Request'}, tags=['SIM/DOREXT']
)
@swagger_auto_schema(
    methods=['DELETE'], operation_summary='Deleta dados do DOREXT', operation_description='Deleta dados de acordo com os parâmetros informados.',
    manual_parameters=[year_param_delete], tags=['SIM/DOREXT'], responses={204: 'No Content', 400: 'Bad Request'}
)
@api_view(['GET', 'POST', 'DELETE'])
def handle_request_dorext(request, format=None):
    return handle_request(request, 'DOREXT', format)


def handle_request(request, prefix, format=None):
    if request.method == 'GET':
        return get(request, prefix, format)
    elif request.method == 'POST':
        return insert(request, prefix, format)
    elif request.method == 'DELETE':
        return delete(request, prefix, format)


def insert(request, prefix, format=None):
    uf = request.GET.get('uf', '')
    year = request.GET.get('year')
    year_file = year

    if any(map(lambda x: x is None, [uf, year])):
        return Response({'message': 'The uf and year parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    uf = uf.upper()

    if prefix in ['DOEXT', 'DOFET', 'DOINF', 'DOMAT', 'DOREXT']:
        year_file = year[2:]
        
    filename = f'{prefix}{uf}{year_file}'

    dbo = PostgresDbOperations(TABLE_NAMES[prefix])
    inserted_files = dbo.get_inserted_files()
    if filename in inserted_files:
        return Response({'message': f'The {filename} file has already been inserted'}, status=status.HTTP_409_CONFLICT)
    
    if int(year) > 1995:
        base_name = 'SIM1'
    else:
        base_name = 'SIM2'

    try:
        download_file(base_name, filename, prefix)
        dbo.insert_file(filename, prefix, uf, year)

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