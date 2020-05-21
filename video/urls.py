from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.awemes, name='awemes'),
    path('<int:user_id>/fetch_awemes', views.fetch_awemes, name='fetch_awemes'),
]