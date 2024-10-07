from django.urls import path
from rest_framework.routers import DefaultRouter


from network.apps import NetworkConfig
from network.views import PlantViewSet, ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView, NetworkViewSet, EntrepreneurViewSet

app_name = NetworkConfig.name
router = DefaultRouter()
router.register(r'plant', PlantViewSet, basename='plant')
router.register(r'network', NetworkViewSet, basename='network')
router.register(r'entrepreneur', EntrepreneurViewSet, basename='entrepreneur')

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDestroyAPIView.as_view(), name='product_delete'),
] + router.urls
