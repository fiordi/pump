import django_filters
from rest_framework import viewsets, permissions, filters, generics
from course.model_classes.SingleLesson import SingleLesson
from course.REST_classes.SingleLessonSerializer import SingleLessonSerializer

"""
SingleLessonViewSet Class
"""
class SingleLessonViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = SingleLesson.objects.all()
	serializer_class = SingleLessonSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('id', 'date', 'course', 'repeatedlesson')
