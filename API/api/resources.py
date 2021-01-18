from import_export import resources
from API.models import Customers, Subscriptions, SellSubscriptions, RegistrationVisits, Staff, Services, KindSport, \
    Rooms, Timetable


class CustomersResource(resources.ModelResource):
    class Meta:
        model = Customers


class SubscriptionsResource(resources.ModelResource):
    class Meta:
        model = Subscriptions


class SellSubscriptionsResource(resources.ModelResource):
    class Meta:
        model = SellSubscriptions


class RegistrationVisitsResource(resources.ModelResource):
    class Meta:
        model = RegistrationVisits


class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff


class ServicesResource(resources.ModelResource):
    class Meta:
        model = Services


class KindSportResource(resources.ModelResource):
    class Meta:
        model = KindSport


class RoomsResource(resources.ModelResource):
    class Meta:
        model = Rooms

class TimetableResource(resources.ModelResource):
    class Meta:
        model = Timetable
