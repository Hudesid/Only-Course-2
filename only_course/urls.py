from django.urls import path
from . import views


urlpatterns = [
    path('', views.InstructorListCreateAPIView.as_view()),
    path('course/list/', views.CourseListCreateAPIView.as_view()),
    path('lesson/list/', views.LessonListCreateAPIView.as_view()),
    path('instructor/detail/<int:pk>/', views.InstructorRetrieveUpdateDestroyAPIView.as_view()),
    path('course/detail/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),
    path('lesson/detail/<int:pk>/', views.LessonRetrieveUpdateDestroyAPIView.as_view())
]