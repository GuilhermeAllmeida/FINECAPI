from django.shortcuts import render,get_object_or_404, redirect
from reserva.models import Reserva,Stand
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from reserva.forms import ReservaForm, StandForm
from django.urls import reverse_lazy
from django.contrib.messages import views

#CRUD RESERVA

class index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context

class listReserva(ListView):
    template_name = 'core/listaReserva.html'
    model = Reserva
    context_object_name = 'reserva'

#criar
class Criar(views.SuccessMessageMixin,CreateView):

    form_class = ReservaForm
    template_name = 'core/formReserva.html'
    success_url = reverse_lazy('listar')
    success_message = "Reserva criada com sucesso!"

class Delete(views.SuccessMessageMixin,DeleteView):
    model = Reserva
    template_name = 'core/confirm.html'
    success_url = reverse_lazy("listar")
    context_object_name= "reserva"
    success_message = "Reserva deletada com sucesso!"

class ReservaUpdateView(views.SuccessMessageMixin,UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("listar")
  template_name = "core/formReserva.html"
  success_message = "Reserva atualizada com sucesso!"

class ReservaDetalhe(DetailView):
    model = Reserva
    template_name = "core/detalheReserva.html"

#CRUD Stand

class listStand(ListView):
    template_name = 'core/listaStand.html'
    model = Stand
    context_object_name = 'stand'

#criar
class Criar(views.SuccessMessageMixin,CreateView):

    form_class = StandForm
    template_name = 'core/formStand.html'
    success_url = reverse_lazy('listar')
    success_message = "Stand criada com sucesso!"

class Delete(views.SuccessMessageMixin,DeleteView):
    model = Stand
    template_name = 'core/confirm.html'
    success_url = reverse_lazy("listar")
    context_object_name= "stand"
    success_message = "Stand deletada com sucesso!"

class StandUpdateView(views.SuccessMessageMixin,UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("listar")
  template_name = "core/formStand.html"
  success_message = "Stand atualizada com sucesso!"

class StandDetalhe(DetailView):
    model = Stand
    template_name = "core/detalheStand.html"