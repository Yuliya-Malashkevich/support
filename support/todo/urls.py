from rest_framework import routers
from .api import TodoViewSet

#создаём роутер по умолчанию и регистрируем апи урл
router = routers.DefaultRouter()
router.register('api/todo', TodoViewSet, 'todo')


urlpatterns = router.urls