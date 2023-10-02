from rest_framework import serializers
from .models import Product, Lesson, LessonView

# Классы сериализаторов для каждой модели

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'all'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = 'all'

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = 'all'