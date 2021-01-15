from django.contrib import admin
from .models import CarSpecs, CarPlan, Categories, Manufacturers, Products, Providers, Supplies, Accounts, Sellers, \
    Customers
from import_export.admin import ImportExportModelAdmin


class CategoriesAdmin(ImportExportModelAdmin):
    search_fields = ('category_name',)


class ProductsAdmin(ImportExportModelAdmin):
    search_fields = ('product_name',)
    list_display = ['product_name', 'product_price']


class CustomersAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'phone_number']


class ManufacturersAdmin(ImportExportModelAdmin):
    search_fields = ('manufacturer_name',)


class ProvidersAdmin(ImportExportModelAdmin):
    search_fields = ('provider_name',)


class SellersAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'position']
    list_filter = ['position']


class SuppliesAdmin(ImportExportModelAdmin):
    list_display = ['provider_id', 'date']
    pass


class AccountsAdmin(ImportExportModelAdmin):
    search_fields = ('product_id', 'seller_id', 'customer_id')
    list_display = ['product_id', 'date', 'seller_id', 'customer_id']
    pass


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Providers, ProvidersAdmin)
admin.site.register(Supplies, SuppliesAdmin)
admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Sellers, SellersAdmin)
