
# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import Document, Text, Date, Search
# from elasticsearch.helpers import bulk
# from elasticsearch import Elasticsearch
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Product, Category


# connections.create_connection(hosts=['localhost'])

# class ProductIndex(Document):
# 	name = Text()
# 	description = Text()
# 	tags = Text()
# 	slug = Text()
# 	created_at = Date()
# 	category = Text()
# 	class Meta:
# 		index = 'productindex'
@registry.register_document
class PrductIndex(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'productindex'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Product
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'slug',
            'description',
            'tags',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000


# def bulk_indexing():
# 	ProductIndex.init()
# 	es = Elasticsearch()
# 	bulk(client=es, actions=(b.indexing() for b in Product.objects.all().iterator()))

# # Simple search function
# def search(name):
# 	s = Search().filter('term', name=name)
# 	response = s.execute()
# 	return response