from rest_framework import serializers
from API.models import Customers, Subscriptions, SellSubscriptions, RegistrationVisits, Staff, Services, KindSport, \
    Rooms, Timetable


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'


class SellSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellSubscriptions
        fields = '__all__'


class RegistrationVisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationVisits
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class KindSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindSport
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'