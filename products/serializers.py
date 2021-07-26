# from rest_framework import serializers, request
# from .models import Product
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     # user = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'tags', 'handle', 'body']
#
#     def validate_title(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Title Value is too short!")
#         return value
#
#
# class ProductPutSerializer(serializers.ModelSerializer):
#     # user = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'tags', 'handle', 'body']
#         read_only_fields = ['handle']
#
#
#
#
#
#
#
#     # def validate_data(self, data):
#     #     if data['handle'] == data['handle']:
#     #         raise serializers.ValidationError("Till death do us part!")
#     #     return data
#
