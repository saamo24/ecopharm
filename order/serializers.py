from rest_framework import serializers
from .models import Order, Checkout

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'medicine', 'quantity']



class OrderSerializer(serializers.ModelSerializer):
    checkout_items = CheckoutSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = [
            'full_name',
            'address',
            'tel',
            'checkout_items'
        ]

    def create(self, validated_data):
        checkout_data = validated_data.pop('checkout_items')
        order = Order.objects.create(**validated_data)

        for checkout_item_data in checkout_data:
            Checkout.objects.create(**checkout_item_data)

        return order
    