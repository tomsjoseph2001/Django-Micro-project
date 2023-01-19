from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('insert/', views.insertData, name="insert"),
    path('update/<str:uname>/', views.updateData, name="update"),
    path('delete/<str:uname>/', views.deleteData, name="delete")

]