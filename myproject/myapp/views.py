from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Product, Lesson, LessonView
from .serializers import ProductSerializer, LessonSerializer, LessonViewSerializer

# Функция для обработки запроса на список уроков по всем продуктам, к которым есть доступ
def lesson_list(request):
    user = request.user
    products = Product.objects.filter(owner=user)
    lessons = Lesson.objects.filter(products__in=products)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

# Функция для обработки запроса на список уроков по конкретному продукту, к которым есть доступ
def lesson_by_product(request):
    user = request.user
    product_id = request.query_params.get('product_id', None)
    if product_id is not None:
        products = Product.objects.filter(owner=user, id=product_id)
        lessons = Lesson.objects.filter(products__in=products)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': 'Missing product_id parameter'}, status=400)

# Функция для вывода статистике по продуктам
def product_statistics(request):
    products = Product.objects.all()
    total_students = User.objects.count()
    data = []
    for product in products:
        lessons = Lesson.objects.filter(products=product)
        total_lessons = lessons.count()
        total_views = LessonView.objects.filter(lesson__in=lessons, status='viewed').count()
        total_duration = LessonView.objects.filter(lesson__in=lessons, status='viewed').aggregate(sum('viewed_time'))['viewed_time__sum']
        total_students_product = LessonView.objects.filter(lesson__in=lessons).values('user').distinct().count()
        percentage = total_students_product / total_students * 100 if total_students > 0 else 0
        product_data = {
            'product': product.name,
            'total_lessons': total_lessons,
            'total_views': total_views,
            'total_duration': total_duration,
            'total_students_product': total_students_product,
            'percentage': percentage
        }
        data.append(product_data)
    return Response(data)