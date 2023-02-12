from django import forms 
from django.forms import ModelForm
from . models import Ticket, Process


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('slug','user',)

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ('slug',)


