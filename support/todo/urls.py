# from django.conf.urls import url
# import views
#
#
# urlpatterns=[
#     url(r'^todo$', views.todoApi),
#     url(r'^todo/([0-9]+)$',views.todoApi)
#  ]


from rest_framework import routers
from .api import TodoViewSet

#создаём роутер по умолчанию и регистрируем апи урл
router = routers.DefaultRouter()
router.register('api/todo', TodoViewSet, 'todo')


urlpatterns = router.urls
