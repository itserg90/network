from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from network.models import Plant, Entrepreneur, Network, Product
from network.serializers import PlantSerializer, NetworkSerializer, EntrepreneurSerializer, ProductSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = DjangoFilterBackend
    filterset_fields = ["country"]

    def has_object_permission(self, request):
        return request.user.is_staff or request.user.is_superuser


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
