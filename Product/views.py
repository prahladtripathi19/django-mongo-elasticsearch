from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from .models import Product, Category, Mostviewed
from .serializers import CategorySerializer, ProductSerializer, MostviewedSerializer
from .documents import PrductIndex
from elasticsearch_dsl import Q

# Create your views here.

class HelloWord(APIView):
	permission_classes = (IsAuthenticated,)
	
	def get(self, request):
		content = {'message': 'Hello, World!=='+self.request.user.email}
		return Response(content)
class CategoryView(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = CategorySerializer
	def get(self, request):
		category = Category.objects.all()
		
		serializer = self.serializer_class(category, many=True)
		return JsonResponse(serializer.data, safe=False)

	def post(self, request):
		name = request.data.get('name')
		published = request.data.get('published')
		slug = name.lower().replace(" ","-")
		catobs = Category.objects.filter(slug=slug)
		if not catobs:
			categoryobs = Category()
			categoryobs.name = name
			categoryobs.slug = slug
			categoryobs.published = int(published)
			categoryobs.updated_at = timezone.now()
			categoryobs.save()
			msg = "category created successfully"
		else:
			msg = "category already exist"



		return JsonResponse({"msg":msg}, safe=False)

class ProductView(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProductSerializer
	def get(self, request):
		products = Product.objects.all()
		serializer = self.serializer_class(products, many=True)
		return JsonResponse(serializer.data, safe=False)


	def post(self, request):
		name = request.data.get('name')
		productcode = request.data.get('productcode')
		price = request.data.get('price')
		published = request.data.get('published')
		category = request.data.get('category')
		slug = name.lower().replace(" ","-")
		description = request.data.get('description')
		tags = request.data.get('tags')
		productobject = Product.objects.filter(slug=slug)
		if not productobject:
			productobs = Product()
			productobs.name = name
			productobs.slug = slug
			productobs.productcode = productcode
			productobs.published = int(published)
			categoryobj = Category.objects.get(id=category)
			productobs.category = categoryobj
			productobs.description = description
			productobs.tags = tags
			productobs.updated_at = timezone.now()
			productobs.save()
			msg = "Product created successfully"
		else:
			msg = "Product already exist"

		return JsonResponse({"msg":msg})
class ProductSearch(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = ProductSerializer
	def get(self,request):
		name = request.GET.get("term")
		#s = PrductIndex.search().filter("match", name=name)
		#s = PrductIndex.search().filter(Q("multi_match", query=name, fields=['name', 'description',]))
		q = Q('bool',
	    must=[Q('match_phrase', name=name)],
	    should=[Q("multi_match", query=name, fields=['name', 'description','tags'])],
	    minimum_should_match=1 )
		s = PrductIndex.search().filter(q)
		productlist = []
		#qs = s.to_queryset()
		#serializer = self.serializer_class(qs, many=True)
		for product in s:
			context = {}
			context["name"] = product.name
			context["slug"] = product.slug
			productlist.append(context)

		return JsonResponse(productlist, safe=False)
class MostViewedProduct(APIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = MostviewedSerializer
	def get(self, request):
		mostviewd = Mostviewed.objects.all().order_by('-view_count')
		
		serializer = self.serializer_class(mostviewd, many=True)
		return JsonResponse(serializer.data, safe=False)

		

