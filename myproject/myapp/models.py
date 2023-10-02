from django.db import models
from django.contrib.auth.models import User

# Сущность продукта
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Сущность урока с ссылкой на сущности продуктов
class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name

# Сущность просмотра
class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_time = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('viewed', 'Viewed'), ('not_viewed', 'Not viewed')])

    def __str__(self):
        return f'{self.username} - {self.lesson.name}'


    # Данная функция предназначена для работы со статусом просмотра видео. Вызов через update_status

    # Получение объекта LessonView
    # lesson_view LessonView.object.get(user=user, lesson=lesson)

    # Обновление времени просмотра
    # lesson_view.viewed_time += view_duration

    # Проверка и обновление статуса
    # lesson_view.update_status()

    def update_status(self):
        if self.viewed_time >= self.lesson.duration * 0.8:
            self.status = 'viewed'
        else:
            self.status = 'not_viewed'
        self.save()