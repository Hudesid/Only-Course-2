from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializers, models

class InstructorListCreateAPIView(ListCreateAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class InstructorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
