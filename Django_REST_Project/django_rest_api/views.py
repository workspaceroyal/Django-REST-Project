# from django.shortcuts import render

from .models import Teacher
from . serializers import TeacherSerializer

from rest_framework import viewsets

from rest_framework.permissions import IsAdminUser

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# from rest_framework.decorators import api_view
# from rest_framework.views import APIView

# from rest_framework.response import Response

# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# import io

# Create your views here.

class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permissions_class = [IsAdminUser]





# class Teacher_LC(ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

# class Teacher_RUD(RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer




# class TeacherLC(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class TeacherRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# class TeacherList(GenericAPIView, ListModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def get(self, request, *args, ** kwargs):
#         return self.list(request, *args, ** kwargs)
#
# class TeacherRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
# class TeacherCreate(GenericAPIView, CreateModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# class TeacherUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
# class TeacherDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)





# class TeacherCreate(APIView):
#     def get(self,request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             # coplex data
#             teacher = Teacher.objects.get(id=id)
#             # python dict
#             serializer = TeacherSerializer(teacher)
#             return Response(serializer.data)
# 
#         # complex data
#         teacher = Teacher.objects.all()
#         # python dict
#         serializer = TeacherSerializer(teacher, many=True)
#         return Response(serializer.data)
# 
#     def post(self,request, format=None):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Successfully insert data'})
#         return Response(serializer.errors)
# 
#     def put(self,request, pk, format=None):
#         id = pk
#         teacher = Teacher.objects.get(pk=id)
#         serializer = TeacherSerializer(teacher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Full data updated'})
#         return Response(serializer.errors)
# 
#     def patch(self,request, pk, format=None):
#         id = pk
#         teacher = Teacher.objects.get(pk=id)
#         serializer = TeacherSerializer(teacher, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial data updated'})
#         return Response(serializer.errors)
# 
#     def delete(self,request, pk, format=None):
#         id = pk
#         teacher = Teacher.objects.get(pk=id)
#         teacher.delete()
#         return Response({'msg': 'Successfully deleted data'})




# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'Delete'])
# def teacher_create(request, pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             #coplex data
#             teacher = Teacher.objects.get(id=id)
#             #python dict
#             serializer = TeacherSerializer(teacher)
#             return Response(serializer.data)
#
#         #complex data
#         teacher = Teacher.objects.all()
#         #python dict
#         serializer = TeacherSerializer(teacher, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Successfully insert data'})
#         return Response(serializer.errors)
#
#     if request.method == 'PUT':
#         id = pk
#         teacher = Teacher.objects.get(pk=id)
#         serializer = TeacherSerializer(teacher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Full data updated'})
#         return Response(serializer.errors)
#
#     if request.method == 'PATCH':
#         id = pk
#         teacher = Teacher.objects.get(pk=id)
#         serializer = TeacherSerializer(teacher, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial data updated'})
#         return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         id = pk
#         teacher = Teacher.objects.get(pk=id)
#         teacher.delete()
#         return Response({'msg': 'Successfully deleted data'})




#Queryset
# def teacher_info(request):
# #complex data
#     teacher = Teacher.objects.all()
#     #python dict
#     serializer = TeacherSerializer(teacher, many=True)
#     # render Json
#     json_data = JSONRenderer().render(serializer.data)
#     #Json sent to User
#     return HttpResponse(json_data, content_type='application/json')

# # Model Instance
# def teacher_ins(request, pk):
#     # complex data
#     teacher = Teacher.objects.get(id=pk)
#     #python dict
#     serializer = TeacherSerializer(teacher)
#     # render Json
#     json_data = JSONRenderer().render(serializer.data)
#     #Json sent to User
#     return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def teacher_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         # json to stream convert
#         stream = io.BytesIO(json_data)
#         # stream to python
#         pythondata = JSONParser().parse(stream)
#         # Python to complex data
#         serializer = TeacherSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Successfully insert data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application.json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application.json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         # json to stream convert
#         stream = io.BytesIO(json_data)
#         # stream to python
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         teacher = Teacher.objects.get(id=id)
#         # Python to complex data
#         serializer = TeacherSerializer(teacher, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Successfully update data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application.json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application.json')
    
#     if request.method == 'DELETE':
#         json_data = request.body
#         # json to stream convert
#         stream = io.BytesIO(json_data)
#         # stream to python
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         teacher = Teacher.objects.get(id=id)
#         teacher.delete()
#         res = {'msg': 'Successfully deleted data'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application.json')
        