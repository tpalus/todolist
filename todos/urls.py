from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('todolist/',views.todoview , name="todo"),
    path("done/<int:pk>",views.Done, name="Done"),
    path("notdone/<int:pk>",views.NotDone, name="NotDone"),
    path("delete/<int:pk>",views.Delete, name="Delete"),
]
