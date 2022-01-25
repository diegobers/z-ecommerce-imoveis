from django.contrib import admin
from django.urls import path, include
from .views import EntrarView, CadastrarView #, OfertaDetail
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('entrar/', EntrarView.as_view(), name='entrar'),
    path('cadastrar/', CadastrarView.as_view(), name='cadastrar'),
    path('sair/', LogoutView.as_view(next_page='home'), name='sair'),
    path('imovel/', include('imovel.urls'))
]
