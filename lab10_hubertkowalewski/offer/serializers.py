from rest_framework import serializers
from .models import Kategoria, Szkolenie

class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = '__all__'

class SzkolenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Szkolenie
        fields = '__all__'