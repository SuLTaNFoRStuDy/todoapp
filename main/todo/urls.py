from django.urls import path
from .views import home, newtodo,delete
urlpatterns = [
    path("",home,name="home"),
    path("newtodo/",newtodo,name="newtodo"),
    path("delete/<int:todo_id>/",delete,name="delete"),
]
