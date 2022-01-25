from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import Imovel 
from django.urls import reverse_lazy


class ImovelList(ListView):
    model = Imovel
    template_name = 'imovel/listar.html'
    context_object_name = 'imoveis'


class ImovelDetail(DetailView):
    model = Imovel
    template_name = 'imovel/detalhes.html'
    context_object_name = 'imovel'


class ImovelCreate(LoginRequiredMixin, CreateView):
    model = Imovel
    template_name = 'imovel/registrar.html'
    context_object_name = 'imovel'
    success_url = reverse_lazy('imoveis')
    fields = '__all__'

    def form_valid(self, form):
        #print('----------oi')
        #form.instance1 =  self.get_queryset().values()#.get(id=1)    #.get(id=2)     # .get_object(self.response_class)
        #print(form.instance1)  
       
        form.instance.cliente = self.request.user
        
        return super(ImovelCreate, self).form_valid(form)



class ImovelUpdate(LoginRequiredMixin, UpdateView):
    model = Imovel
    template_name = 'imovel/registrar.html'
    context_object_name = 'imovel'
    fields = '__all__'
    success_url = reverse_lazy('imoveis')


class ImovelDelete(LoginRequiredMixin, DeleteView):
    model = Imovel
    template_name = 'imovel/deletar.html'
    context_object_name = 'imovel'
    success_url = reverse_lazy('imoveis')
