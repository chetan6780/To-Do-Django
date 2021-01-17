from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_todo/',views.add_todo,name='add_todo'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('delete_todo/<int:todo_id>/',views.delete_todo,name='add_todo'),
    path('contact/add_contact/',views.add_contact,name='add_contact'),
]
