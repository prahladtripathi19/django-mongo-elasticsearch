from rest_framework import serializers
from .models import Product, Category, Mostviewed

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ["id","name","slug","published","created_at","updated_at"]

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ["id","name","slug","productcode","price","published","category","created_at","updated_at"]

class MostviewedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mostviewed
		fields = ["id","product"]

