from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewset, ManufacturersViewset, ProductsViewset, ProvidersViewset, SuppliesViewset, AccountsViewset, SellersViewset, CustomersViewset

router = DefaultRouter()
router.register('categories', CategoriesViewset, basename='categories')
router.register('manufacturers', ManufacturersViewset, basename='manufacturers')
router.register('products', ProductsViewset, basename='products')
router.register('providers', ProvidersViewset, basename='providers')
router.register('supplies', SuppliesViewset, basename='supplies')
router.register('accounts', AccountsViewset, basename='accounts')
router.register('sellers', SellersViewset, basename='sellers')
router.register('customers', CustomersViewset, basename='customers')
urlpatterns = router.urls


