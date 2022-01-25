from django.urls import path
from . import views
from .views import ImovelList, ImovelCreate, ImovelDetail, ImovelUpdate, ImovelDelete


urlpatterns = [
    path('', ImovelList.as_view(), name='imoveis'),

    path('detalhes/<int:pk>/', ImovelDetail.as_view(), name='detalhar-imovel'),
    path('alterar/<int:pk>/', ImovelUpdate.as_view(), name='alterar-imovel'),
    path('deletar/<int:pk>/', ImovelDelete.as_view(), name='deletar-imovel'),
    path('registrar/', ImovelCreate.as_view(), name='registrar-imovel'),
]