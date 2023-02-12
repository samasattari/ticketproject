from django.urls import path, include
from .views import ticket_views, process_views

urlpatterns = [
    path('ticket/', ticket_views.as_view() , name='ticketviews'),
    path('process/', process_views.as_view(), name='processviews')
    ]