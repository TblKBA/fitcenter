from import_export import resources
from firstApp.models import Categories, Manufacturers, Products, Providers, Supplies, Accounts, Sellers, Customers


class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories


class ManufacturersResource(resources.ModelResource):
    class Meta:
        model = Manufacturers


class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products


class ProvidersResource(resources.ModelResource):
    class Meta:
        model = Providers


class SuppliesResource(resources.ModelResource):
    class Meta:
        model = Supplies


class AccountsResource(resources.ModelResource):
    class Meta:
        model = Accounts


class SellersResource(resources.ModelResource):
    class Meta:
        model = Sellers


class CustomersResource(resources.ModelResource):
    class Meta:
        model = Customers

