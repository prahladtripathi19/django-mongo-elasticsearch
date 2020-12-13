from django.db import models
from datetime import datetime
# from .documents import ProductIndex


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

class Product(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	description = models.TextField(default="")
	tags = models.CharField(max_length=100, blank=True, default="")
	productcode = models.CharField(max_length=100, unique=True)
	price = models.IntegerField(default=0)
	published = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# def indexing(self):
	# 	obj = ProductIndex(
	# 	    meta={'id': self.id},
	# 	    category=self.category.slug,
	# 	    created_at=self.created_at,
	# 	    name=self.name,
	# 	    description=self.description,
	# 	    tags = self.tags,
	# 	    slug=self.slug
	# 	)
	# 	obj.save()
	# 	return obj.to_dict(include_meta=True)

class Mostviewed(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	view_count = models.IntegerField(default=0)
