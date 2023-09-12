from rest_framework import serializers
from .models import Medicine

class MedicineGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = [
            'id',
            'name',
            'price',
            'quantity',
            'image',
        ]
