from django.urls import path
from . import views #esse ponto é porque é do mesmo diretorio blog

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

