#urls.py
from django.urls import path
from .views import HelloWord, CategoryView, ProductView, ProductSearch, MostViewedProduct

urlpatterns = [

    path('check/', HelloWord.as_view(), name='hello'),
    path('category/', CategoryView.as_view(), name='category_view'),
    path('product/', ProductView.as_view(), name='product_view'),
    path('product-search/', ProductSearch.as_view(), name='product_search'),
    path('most-viewed-product/', MostViewedProduct.as_view(), name='MostViewedProduct'),

]