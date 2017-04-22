from django.views import generic
from django.views.generic.edit import CreateView,DeleteView, UpdateView
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from .models import Ticket


class DetailView(generic.ListView):
	template_name='complaint/detail.html'
	context_object_name='tics'

	def get_queryset(self):
		return Ticket.objects.all()


def Index(request):
	return render(request, 'complaint/index.html')


class TicketCreate(CreateView):
	model= Ticket
	fields=['firstname','lastname','device','status']

class TicketUpdate(UpdateView):
	model= Ticket
	fields=['firstname','lastname','device','status']

class TicketDelete(DeleteView):
	model=Ticket
	success_url=reverse_lazy('complaint:detail')


