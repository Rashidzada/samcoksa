from rest_framework import viewsets

from .serializers import *
from .models import *


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ContactUViewSet(viewsets.ModelViewSet):
    queryset = ContactU.objects.all()
    serializer_class = ContactUSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TeamViewSet(viewsets.ModelViewSet):
     queryset =Team.objects.all()
     serializer_class = TeamSerializer
