from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactU
        fields = "__all__"


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Service
          fields = '__all__'

