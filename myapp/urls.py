from django.urls import path
from . import views

urlpatterns = [
    path('', views.User, name="login"),
    path('sign_up/', views.register_view, name="sign_up"),
    path('home/', views.home, name="home"),
    path('planner/', views.planner, name="planner"),
    path('create/', views.create, name='create'),
    path('comment/', views.comment, name='comment'),
    path('delete/<int:id>', views.delete_todo, name='delete_todo'),
    path('logout/', views.log_out, name="logout"),

   ]