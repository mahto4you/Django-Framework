from django.urls import path
from . import views
urlpatterns = [
    path('learndj/', views.learn_django),
    path('learndj2/', views.learn_django2),
]
