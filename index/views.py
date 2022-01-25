from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from imovel.models import Imovel
#from django.views.generic.detail import DetailView

#class HomeView(TemplateView):
#    template_name = 'index/home.html'


def home(request):
    imoveis = Imovel.objects.all()

    return render(request, 'home.html', {'imoveis': imoveis})

class EntrarView(LoginView):
    template_name = 'index/entrar.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CadastrarView(FormView):
    template_name = 'index/cadastrar.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(CadastrarView, self).form_valid(form)
    # return view if is_authenticated
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')    
        return super(CadastrarView, self).get(*args, **kwargs)    
        