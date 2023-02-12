from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import TicketForm, ProcessForm

class ticket_views(CreateView):
    form_class = TicketForm
    template_name = 'ticket/ticket.html'
    success_url = '/admin/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user= self.request.user
        return super(ticket_views, self).form_valid(form)
    
    
class process_views(CreateView):
    form_class = ProcessForm
    template_name = 'ticket/process.html'
    success_url = '/admin/'

    
