from rest_framework import serializers
from network.models import Plant, Product, Network, Entrepreneur


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    plant = PlantSerializer(read_only=True)

    class Meta:
        model = Network
        fields = '__all__'


class EntrepreneurSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Entrepreneur
        fields = '__all__'
