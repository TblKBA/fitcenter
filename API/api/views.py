from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrReadOnly
from rest_framework import viewsets
from .serializer import CategoriesSerializer, ManufacturersSerializer, ProductsSerializer, ProvidersSerializer, SuppliesSerializer, AccountsSerializer, SellersSerializer, CustomersSerializer
from API.models import CarSpecs, CarPlan, Categories, Manufacturers, Products, Providers, Supplies, Accounts, Sellers, Customers


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    # print(request.query_params)
    return Response({'message': "we received"})


@permission_classes([IsAdminOrReadOnly])
class CategoriesViewset(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        categories = Categories.objects.all()
        return categories


@permission_classes([IsAdminOrReadOnly])
class ManufacturersViewset(viewsets.ModelViewSet):
    serializer_class = ManufacturersSerializer

    def get_queryset(self):
        manufacturers = Manufacturers.objects.all()
        return manufacturers


@permission_classes([IsAdminOrReadOnly])
class ProductsViewset(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        products = Products.objects.all()
        return products


@permission_classes([IsAdminOrReadOnly])
class ProvidersViewset(viewsets.ModelViewSet):
    serializer_class = ProvidersSerializer

    def get_queryset(self):
        providers = Providers.objects.all()
        return providers


@permission_classes([IsAdminOrReadOnly])
class SuppliesViewset(viewsets.ModelViewSet):
    serializer_class = SuppliesSerializer

    def get_queryset(self):
        supplies = Supplies.objects.all()
        return supplies


@permission_classes([IsAdminOrReadOnly])
class AccountsViewset(viewsets.ModelViewSet):
    serializer_class = AccountsSerializer

    def get_queryset(self):
        accounts = Accounts.objects.all()
        return accounts


@permission_classes([IsAdminOrReadOnly])
class SellersViewset(viewsets.ModelViewSet):
    serializer_class = SellersSerializer

    def get_queryset(self):
        sellers = Sellers.objects.all()
        return sellers


@permission_classes([IsAdminOrReadOnly])
class CustomersViewset(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer

    def get_queryset(self):
        customers = Customers.objects.all()
        return customers
