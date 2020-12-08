# serializers.py
from rest_framework import serializers

from .models import Hero
from .models import Diamond

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')

class DiamondSerializer(serializers.ModelSerializer):
            class Meta:
                model = Diamond
                fields = ('color', 'cut', 'clarity', 'caratWeight')