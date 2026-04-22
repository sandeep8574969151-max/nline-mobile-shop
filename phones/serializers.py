from rest_framework import serializers
from .models import Phone, Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class PhoneSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Phone
        fields = '__all__'