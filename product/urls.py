from django.urls import path

from .views import LatestProductsList
from .views import ProductDetail

urlpatterns = [
  path('latest-products/', LatestProductsList.as_view()),
  path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
]