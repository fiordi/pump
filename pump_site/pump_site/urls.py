"""pump_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pump_app.views import Debug

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^debug/', Debug.as_view()),
]

#requests for ManageCourseHandler controller
from pump_app.views import ManageCourseHandler

urlpatterns.extend([
    url(r'^course/makenewcourse', ManageCourseHandler().makeNewCourse),
    url(r'^course/activatecourse/(\w+)/$', ManageCourseHandler().activateCourse),
    url(r'^lesson/addlesson', ManageCourseHandler().addLesson),
    url(r'^lesson/savecourse/(\w+)/$', ManageCourseHandler().saveCourse)
])


#requests for ManageCourseHandler controller to be redirected to REST FRAMEWORK
from rest_framework import routers
from django.conf.urls import url, include
from pump_app.REST_classes.CourseCatalogViewSet import CourseCatalogViewSet

router = routers.DefaultRouter()
router.register(r'course', ManageCourseHandler().setCourseInfo(base_name='course'))
router.register(r'lesson', ManageCourseHandler().setLessonInfo(base_name='lesson'))


urlpatterns.extend([
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])
