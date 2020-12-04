from django.urls import path
from enroll import views
urlpatterns = [
    #path('student/1/', views.show_details, name='detail')
    #path('student/<my_id>/', views.show_details, name='detail')
    path('<int:my_id>/', views.show_details, name='detail'),
    path('<int:my_id>/<int:my_subid>/', views.show_subdetails, name='subdetail'),
]