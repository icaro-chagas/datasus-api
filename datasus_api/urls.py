from django.contrib import admin
from django.urls import path
from datasus_api.views import views_cnes
from datasus_api.views import views_siasus
from datasus_api.views import views_cih
from datasus_api.views import views_ciha
from datasus_api.views import views_pce
from datasus_api.views import views_po
from datasus_api.views import views_resp
from datasus_api.views import views_sihsus
from datasus_api.views import views_doc
from datasus_api.views import views_sim

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="DATASUS API",
        default_version='v1',
        description="API que disponibiliza dados do DATASUS",
        contact=openapi.Contact(email="icaro.almeida@ccc.ufcg.edu.br"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('cih/cr', views_cih.handle_request_cr),
    path('ciha', views_ciha.handle_request_ciha),
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
    path('pce', views_pce.handle_request_pce),
    path('po', views_po.handle_request_po),
    path('resp', views_resp.handle_request_resp),
    path('siasus/ab', views_siasus.handle_request_ab),
    path('siasus/abo', views_siasus.handle_request_abo),
    path('siasus/acf', views_siasus.handle_request_acf),
    path('siasus/ad', views_siasus.handle_request_ad),
    path('siasus/am', views_siasus.handle_request_am),
    path('siasus/an', views_siasus.handle_request_an),
    path('siasus/aq', views_siasus.handle_request_aq),
    path('siasus/ar', views_siasus.handle_request_ar),
    path('siasus/atd', views_siasus.handle_request_atd),
    path('siasus/pa', views_siasus.handle_request_pa),
    path('siasus/ps', views_siasus.handle_request_ps),
    path('siasus/sad', views_siasus.handle_request_sad),
    path('sihsus/er', views_sihsus.handle_request_er),
    path('sihsus/rd', views_sihsus.handle_request_rd),
    path('sihsus/rj', views_sihsus.handle_request_rj),
    path('sihsus/sp', views_sihsus.handle_request_sp),
    path('sim/do', views_sim.handle_request_do),
    path('sim/doext', views_sim.handle_request_doext),
    path('sim/dofet', views_sim.handle_request_dofet),
    path('sim/doinf', views_sim.handle_request_doinf),
    path('sim/domat', views_sim.handle_request_domat),
    path('sim/dorext', views_sim.handle_request_dorext),
    path('datasus-doc', views_doc.get_doc),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]