from drf_yasg import openapi

uf_param_post = openapi.Parameter(
    name='uf',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='UF (Unidade Federativa)',
    required=True,
    min_length=2,
    max_length=2
)

month_param_post = openapi.Parameter(
    name='month',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Número do mês',
    required=True,
    min_length=1,
    max_length=2
)

year_param_post = openapi.Parameter(
    name='year',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Ano',
    required=True,
    min_length=4,
    max_length=4
)

letter_param_post = openapi.Parameter(
    name='letter',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Partição do dado (Ex: a, b, c, ...)',
    required=False,
    min_length=1,
    max_length=1
)


uf_param_get = openapi.Parameter(
    name='uf',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='UF (Unidade Federativa)',
    required=False,
    min_length=2,
    max_length=2
)

month_param_get = openapi.Parameter(
    name='month',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Número do mês',
    required=False,
    min_length=1,
    max_length=2
)

year_param_get = openapi.Parameter(
    name='year',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Ano',
    required=False,
    min_length=4,
    max_length=4
)

uf_param_delete = openapi.Parameter(
    name='uf',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='UF (Unidade Federativa)',
    required=True,
    min_length=2,
    max_length=2
)

month_param_delete = openapi.Parameter(
    name='month',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Número do mês',
    required=False,
    min_length=1,
    max_length=2
)

year_param_delete = openapi.Parameter(
    name='year',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Ano',
    required=False,
    min_length=4,
    max_length=4
)


db_name_param_get = openapi.Parameter(
    name='db_name',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Sigla da base de dados',
    required=True,
    min_length=2,
    max_length=4
)

table_name_param_get = openapi.Parameter(
    name='table_name',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Sigla da tabela',
    required=True,
    min_length=2,
    max_length=4
)