from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import serializers, models

class InstructorListCreateAPIView(ListCreateAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def perform_create(self, serializer):
        teacher_name = self.request.data.get('teacher')
        if teacher_name:
            teacher_instance = get_object_or_404(models.Instructor, name=teacher_name)
            serializer.save(teacher=teacher_instance)
        else:
            serializer.save()


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

    def perform_create(self, serializer):
        course = self.request.data.get('course')
        if course:
            course_instance = get_object_or_404(models.Course, title=course)
            serializer.save(course=course_instance)
        else:
            serializer.save()


class InstructorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
