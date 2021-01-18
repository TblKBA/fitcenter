from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrReadOnly
from rest_framework import viewsets
from .serializer import CustomersSerializer, SubscriptionsSerializer, SellSubscriptionsSerializer, \
    RegistrationVisitsSerializer, StaffSerializer, ServicesSerializer, KindSportSerializer, RoomsSerializer, \
    TimetableSerializer
from API.models import Customers, Subscriptions, SellSubscriptions, RegistrationVisits, Staff, Services, KindSport, \
    Rooms, Timetable


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    # print(request.query_params)
    return Response({'message': "we received"})


@permission_classes([IsAdminOrReadOnly])
class CustomersViewset(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer

    def get_queryset(self):
        customers = Customers.objects.all()
        return customers


@permission_classes([IsAdminOrReadOnly])
class SubscriptionsViewset(viewsets.ModelViewSet):
    serializer_class = SubscriptionsSerializer

    def get_queryset(self):
        subscriptions = Subscriptions.objects.all()
        return subscriptions


@permission_classes([IsAdminOrReadOnly])
class SellSubscriptionsViewset(viewsets.ModelViewSet):
    serializer_class = SellSubscriptionsSerializer

    def get_queryset(self):
        sellSubscriptions = SellSubscriptions.objects.all()
        return sellSubscriptions


@permission_classes([IsAdminOrReadOnly])
class RegistrationVisitsViewset(viewsets.ModelViewSet):
    serializer_class = RegistrationVisitsSerializer

    def get_queryset(self):
        registrationVisits = RegistrationVisits.objects.all()
        return registrationVisits


@permission_classes([IsAdminOrReadOnly])
class StaffViewset(viewsets.ModelViewSet):
    serializer_class = StaffSerializer

    def get_queryset(self):
        staff = Staff.objects.all()
        return staff


@permission_classes([IsAdminOrReadOnly])
class ServicesViewset(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        services = Services.objects.all()
        return services


@permission_classes([IsAdminOrReadOnly])
class KindSportViewset(viewsets.ModelViewSet):
    serializer_class = KindSportSerializer

    def get_queryset(self):
        kindSport = KindSport.objects.all()
        return kindSport


@permission_classes([IsAdminOrReadOnly])
class RoomsViewset(viewsets.ModelViewSet):
    serializer_class = RoomsSerializer

    def get_queryset(self):
        rooms = Rooms.objects.all()
        return rooms


@permission_classes([IsAdminOrReadOnly])
class TimetableViewset(viewsets.ModelViewSet):
    serializer_class = TimetableSerializer

    def get_queryset(self):
        timetable = Timetable.objects.all()
        return timetable