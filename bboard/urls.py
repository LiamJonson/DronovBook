from django.urls import path
from .views import index
from .views import index, by_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),#послед-именов маршрут
    path('', index, name='index'),
]
