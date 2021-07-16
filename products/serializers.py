from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'handle', 'body']

    def validate_title(self, value):
        if len(value) < 3 :
            raise serializers.ValidationError("Title Value is too short!")
        return value


class ProductPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'body']


