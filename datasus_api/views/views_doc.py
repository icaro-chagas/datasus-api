from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..util.datasus_util import download_file
from drf_yasg.utils import swagger_auto_schema
from ..util.doc_datasus_util import dict_datasus
from ..util.doc_api_util import db_name_param_get, table_name_param_get


@swagger_auto_schema(
    methods=['GET'], operation_summary='Fornece documentação do DATASUS', operation_description='Fornece documentação para cada tabela do DATASUS de acordo com os parâmetros informados.',
    manual_parameters=[db_name_param_get, table_name_param_get], responses={200: 'OK', 400: 'Bad Request'}, tags=['DOC DATASUS']
)
@api_view(['GET'])
def get_doc(request):
    db_name = request.GET.get('db_name', '')
    table_name = request.GET.get('table_name', '')

    db_name = db_name.upper()
    table_name = table_name.upper()

    if any(map(lambda x: x is None, [db_name, table_name])):
        return Response({'message': 'The db_name and table_name parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if (db_name, table_name) not in dict_datasus:
        return Response({'message': 'The db_name or table_name is invalid'}, status=status.HTTP_400_BAD_REQUEST)
    
    dict_doc = dict_datasus[(db_name, table_name)]
    
    return Response(dict_doc, status=status.HTTP_200_OK)
