"""
URL configuration for Django_REST_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_rest_api import views

from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register
router.register('teacher_url', views.TeacherModelViewSet,
basename='teacher')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pai-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

    # path('teacher-info/', views.teacher_info),
    # path('teacher-info/<int:pk>', views.teacher_ins),

    # path('teacher-create/', views.teacher_create, name='teacher-create'),
    # path('teacher-create/<int:pk>', views.teacher_create, name='teacher-create'),

    # path('teacher-create/', views.TeacherCreate.as_view(), name='teacher-create'),
    # path('teacher-create/<int:pk>', views.TeacherCreate.as_view(), name='teacher-create'),

    # path('teacher-list/', views.TeacherList.as_view(), name='teacher-list'),
    # path('teacher-retrieve/<int:pk>', views.TeacherRetrieve.as_view(), name='teacher-retrieve'),
    # path('teacher-create/', views.TeacherCreate.as_view(), name='teacher-create'),
    # path('teacher-update/<int:pk>', views.TeacherUpdate.as_view(), name='teacher-update'),
    # path('teacher-destroy/<int:pk>', views.TeacherDestroy.as_view(), name='teacher-destroy'),

    # path('teacher-lc/', views.TeacherLC.as_view(), name='teacher-lc'),
    # path('teacher-lc/<int:pk>', views.TeacherRUD.as_view(), name='teacher-rud'),
    
    # path('teacher-lc/', views.Teacher_LC.as_view(), name='teacher-lc'),
    # path('teacher-lc/<int:pk>', views.Teacher_RUD.as_view(), name='teacher-rud'),
]
