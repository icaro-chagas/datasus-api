from django.http import JsonResponse
from django.core.paginator import Paginator
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

MAX_ROWS_PER_PAGE = 200000

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


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ee(request, format=None):
    return handle_request(request, 'EE', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_dc(request, format=None):
    return handle_request(request, 'DC', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ef(request, format=None):
    return handle_request(request, 'EF', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_ep(request, format=None):
    return handle_request(request, 'EP', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_eq(request, format=None):
    return handle_request(request, 'EQ', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_gm(request, format=None):
    return handle_request(request, 'GM', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_hb(request, format=None):
    return handle_request(request, 'HB', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_in(request, format=None):
    return handle_request(request, 'IN', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_lt(request, format=None):
    return handle_request(request, 'LT', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_pf(request, format=None):
    return handle_request(request, 'PF', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_rc(request, format=None):
    return handle_request(request, 'RC', format)


@api_view(['GET', 'POST', 'DELETE'])
def handle_request_sr(request, format=None):
    return handle_request(request, 'SR', format)


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