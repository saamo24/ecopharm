from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.response import Response

from .models import Order, Checkout
from .serializers import OrderSerializer, CheckoutSerializer

class OrderAPIView(views.APIView):

    serializer_class = OrderSerializer

    def get(self, request):
        queryset = Order.objects.all()
        orders = OrderSerializer(queryset, many=True)

        return Response(orders.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        resp = self.serializer_class(order)
        return Response(resp.data, status=status.HTTP_201_CREATED)


class OrderDetailAPIView(views.APIView):

    serializer_class = OrderSerializer

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        order_data = OrderSerializer(order)
        return Response(order_data.data)

class CheckoutAPIView(views.APIView):

    serializer_class = CheckoutSerializer

    def get(self, request):
        queryset = Checkout.objects.all()
        checkouts = CheckoutSerializer(queryset, many=True)
        return Response(checkouts.data)
    

    def post(self, request):
        # Create a copy of the request data
        request_data = request.data.copy()

        # Create a default order if order_id is not provided in the request
        order_id = request_data.pop('order_id', None)
        if order_id is None:
            # Create a default order here
            default_order = Order.objects.create(full_name="Default Order", address="Default Address", tel="Default Phone")
            order_id = default_order.id

        # Add the order_id to the modified request data
        request_data['order_id'] = order_id

        serializer = self.serializer_class(data=request_data)
        serializer.is_valid(raise_exception=True)
        checkout = serializer.save()
        resp = self.serializer_class(checkout)
        return Response(resp.data, status=status.HTTP_201_CREATED)
