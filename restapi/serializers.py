from rest_framework import serializers
from .models import Drinks

class DrinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'description'] 