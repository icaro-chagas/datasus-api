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


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ab(request, format=None):
    return handle_request(request, 'AB', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_abo(request, format=None):
    return handle_request(request, 'ABO', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_acf(request, format=None):
    return handle_request(request, 'ACF', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ad(request, format=None):
    return handle_request(request, 'AD', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_am(request, format=None):
    return handle_request(request, 'AM', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_an(request, format=None):
    return handle_request(request, 'AN', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_aq(request, format=None):
    return handle_request(request, 'AQ', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ar(request, format=None):
    return handle_request(request, 'AR', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_atd(request, format=None):
    return handle_request(request, 'ATD', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_pa(request, format=None):
    return handle_request(request, 'PA', format)

@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ps(request, format=None):
    return handle_request(request, 'PS', format)

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