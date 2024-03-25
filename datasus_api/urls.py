from django.contrib import admin
from django.urls import path
from datasus_api.views import views_cnes
from datasus_api.views import views_siasus
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cnes/dc', views_cnes.handle_request_dc),
    path('cnes/ee', views_cnes.handle_request_ee),
    path('cnes/ef', views_cnes.handle_request_ef),
    path('cnes/ep', views_cnes.handle_request_ep),
    path('cnes/eq', views_cnes.handle_request_eq),
    path('cnes/gm', views_cnes.handle_request_gm),
    path('cnes/hb', views_cnes.handle_request_hb),
    path('cnes/in', views_cnes.handle_request_in),
    path('cnes/lt', views_cnes.handle_request_lt),
    path('cnes/pf', views_cnes.handle_request_pf),
    path('cnes/rc', views_cnes.handle_request_rc),
    path('cnes/sr', views_cnes.handle_request_sr),
    path('siasus/pa', views_siasus.handle_request_pa),
]

urlpatterns = format_suffix_patterns(urlpatterns)