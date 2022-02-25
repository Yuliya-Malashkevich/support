from django.db import models

# Create your models herе, котрая будет храниться в бд cо следующими  полями

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)


#строковое представление по названию (title)
    def __str__(self):
        return self.title
#дальше регистрируем эту модель в админке

