from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet

from .models import Product, Firm, Category
from .serializers import CategorySerializer, ProductSerializer, FirmSerializer


# Create your views here.


class ProductGenericViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FirmGenericViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class CategoryGenericViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
