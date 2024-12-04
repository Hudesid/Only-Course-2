from rest_framework import serializers
from . import models

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ('id', 'name', 'email', 'specialty')

    def validate(self, data):
        email = data.get('email')
        instructor_id = data.get('id')
        email_instance = models.Instructor.objects.filter(email=email).exists()

        if email_instance and instructor_id != email_instance.id:
            raise serializers.ValidationError({"email": "Bu email manzil allaqachon mavjud."})
        return data


class CourseSerializer(serializers.ModelSerializer):
    teacher = InstructorSerializer(read_only=True)

    class Meta:
        model = models.Course
        fields = ('id', 'title', 'description', 'start_at', 'end_at', 'teacher')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['teacher'] = InstructorSerializer(instance.courses).data
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        if 'teacher' in data:
            try:
                teacher = models.Instructor.objects.get(id=data['teacher'])
                internal_value['teacher'] = teacher
            except models.Instructor.DoesNotExist:
                raise serializers.ValidationError({'teacher': 'Invalid teacher ID.'})
        return internal_value

    def validate(self, data):
        start_at = data.get('start_at')
        end_at = data.get('end_at')

        if start_at and end_at and start_at > end_at:
            raise serializers.ValidationError({
                'non_field_errors': "Kursning boshlanish sanasi tugash sanasidan oldin bo'lishi kerak.",
            })

        return data

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('id', 'title', 'description', 'course', 'order')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['courses'] = CourseSerializer(instance.courses).data
        return representation

    def validate_order(self, value):
        if value < 0 :
            raise serializers.ValidationError({"order" : "Tartib raqami musbat butun son bo'lishi kerak."})
        return value