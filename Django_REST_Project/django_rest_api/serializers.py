from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']

# class TeacherSerializer(serializers.Serializer):
#     teacher_name = serializers. CharField(max_length=25)
#     course_name = serializers.CharField(max_length=20)
#     course_duration = serializers. IntegerField()
#     seat = serializers.IntegerField()

#     def create(self, validated_data):
#         return Teacher.objects.create( ** validated_data)

#     def update(self, instance, validated_data):
#         instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
#         instance.course_name = validated_data.get('course_name', instance.course_name)
#         instance.course_duration = validated_data.get('course_duration', instance.course_duration)
#         instance.seat = validated_data.get('seat', instance.seat)
#         instance.save()
#         return instance
