from rest_framework import serializers, request
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'handle', 'body']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title Value is too short!")
        return value


class ProductPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'handle', 'body']
        read_only_fields = ['handle']
