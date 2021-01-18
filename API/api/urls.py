from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CustomersViewset, SubscriptionsViewset, SellSubscriptionsViewset, RegistrationVisitsViewset, \
    StaffViewset, ServicesViewset, KindSportViewset, RoomsViewset, TimetableViewset

router = DefaultRouter()
router.register('customers', CustomersViewset, basename='customers')
router.register('subscriptions', SubscriptionsViewset, basename='subscriptions')
router.register('sellSubscriptions', SellSubscriptionsViewset, basename='sellSubscriptions')
router.register('registrationVisits', RegistrationVisitsViewset, basename='registrationVisits')
router.register('staff', StaffViewset, basename='staff')
router.register('services', ServicesViewset, basename='services')
router.register('kindSport', KindSportViewset, basename='kindSport')
router.register('rooms', RoomsViewset, basename='rooms')
router.register('timetable', TimetableViewset, basename='timetable')
urlpatterns = router.urls


