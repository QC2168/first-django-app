from django.urls import path
from . import views
app_name = "todolist"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete')
]
