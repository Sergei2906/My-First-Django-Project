from django.urls import path
from .views import lesson_list, lesson_by_product, product_statistics

urlpatterns = [
    path('lessons/', lesson_list, name='lesson_list'),
    path('lessons/by_product/', lesson_by_product, name='lesson_by_product'),
    path('products/statistics/', product_statistics, name='product_statistics'),
]