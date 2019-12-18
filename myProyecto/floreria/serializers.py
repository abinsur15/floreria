from rest_framework import serializers
from .models import Flor

class florserializer(serializers.ModelSerializer):
    class Meta:
        model = Flor
        fields = ['nombre','descripcion','valor']