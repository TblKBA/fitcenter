from django.contrib import admin
from .models import Customers, Subscriptions, SellSubscriptions, Staff, Services, KindSport, Rooms, Timetable, \
     RegistrationVisits
from import_export.admin import ImportExportModelAdmin

class CustomersAdmin(ImportExportModelAdmin):
     search_fields = ('phone',)
     list_display = ['fio', 'address']

class SubscriptionsAdmin(ImportExportModelAdmin):
     search_fields = ('subscription_name',)
     list_display = ['price', 'days']

class SellSubscriptionsAdmin(ImportExportModelAdmin):
     search_fields = ('customer_id',)
     list_display = ['subscription_id', 'date_end']

class StaffAdmin(ImportExportModelAdmin):
     search_fields = ('fio',)
     list_display = ['address', 'salary']

class ServicesAdmin(ImportExportModelAdmin):
     search_fields = ('service_name',)

class KindSportAdmin(ImportExportModelAdmin):
     search_fields = ('staff_id', 'service_id')
     list_display = ['note']

class RoomsAdmin(ImportExportModelAdmin):
     search_fields = ('room_name',)

class TimetableAdmin(ImportExportModelAdmin):
     search_fields = ('timetable_date',)
     list_display = ['start_time', 'end_time']

class RegistrationVisitsAdmin(ImportExportModelAdmin):
     search_fields = ('sellSubscription_id',)
     list_display = ['timetable_id']


admin.site.register(Customers, CustomersAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)
admin.site.register(SellSubscriptions, SellSubscriptionsAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(KindSport, KindSportAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(RegistrationVisits, RegistrationVisitsAdmin)


