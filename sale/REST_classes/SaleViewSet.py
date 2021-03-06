from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from sale.model_classes.Sale import Sale
from sale.REST_classes.SaleSerializer import SaleSerializer, SaleSerializer_packets_field
from collections import Counter
import datetime, json


"""
SaleViewSet Class
"""
class SaleViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

	queryset = Sale.objects.all()
	serializer_class = SaleSerializer






	"""
	It overrides the default __retrieve()__ method of REST API for customizaton (amount must be update on every reload)

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	def retrieve(self, request, pk=None):
		from sale.model_classes.ManageSaleHandler import ManageSaleHandler

		queryset = Sale.objects.all()
		sale = get_object_or_404(queryset, pk=pk)

		serializer = SaleSerializer(sale)
		return Response(serializer.data)









	"""
	It overrides the default __create()__ method of REST API in order to create a new sale and put into it a timeStamp of
	starting dateTime and the User linked to the sale

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	def create(self, request, pk=None):
		from sale.model_classes.ManageSaleHandler import ManageSaleHandler

		serializer = SaleSerializer(data=request.data)

		logged_user = request.user

		if serializer.is_valid() and logged_user.is_authenticated():
			sale = ManageSaleHandler().makeNewSale(logged_user)

		serializer = SaleSerializer(sale)
		return Response(serializer.data)




	"""
	It creates a new route rule which checks if Sale can be completed and, if so, creates a new Subscription or updates existing

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	@detail_route(methods=['get'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def confirm_sale(self, request, pk=None):
		from sale.model_classes.ManageSaleHandler import ManageSaleHandler

		queryset = Sale.objects.all()
		sale = get_object_or_404(queryset, pk=pk)

		#checks (to be written)
		#...
		#...

		customer = request.user.customer


		sale = ManageSaleHandler().confirmSale(customer, sale)


		serializer = SaleSerializer(sale)
		return Response(serializer.data)






	"""
	It checks if a Packet can be added to a Sale and, if so, does it, calculating the new amount

	request => HttpRequest()
	pk => Integer

	:return Response()
	"""
	@detail_route(methods=['put', 'patch'], permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,))
	def patch_packets(self, request, pk=None):
		from sale.model_classes.ManageSaleHandler import ManageSaleHandler

		queryset = Sale.objects.all()
		sale = get_object_or_404(queryset, pk=pk)

		serializer = SaleSerializer_packets_field(data=request.data)

		if serializer.is_valid():
			packets_sale = request.data.get('packets')
			ManageSaleHandler().addPacketList(sale, packets_sale)

		serializer = SaleSerializer(sale)
		return Response(serializer.data)