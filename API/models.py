from django.db import models


class Customers(models.Model):
    fio = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.fio


class Subscriptions(models.Model):
    subscription_name = models.CharField(max_length=150)
    price = models.CharField(max_length=5)
    visits = models.CharField(max_length=5)
    days = models.CharField(max_length=5)

    def __str__(self):
        return self.subscription_name


class SellSubscriptions(models.Model):
    customer_id = models.ForeignKey(
        Customers, on_delete=models.SET_NULL, null=True
    )
    subscription_id = models.ForeignKey(
        Subscriptions, on_delete=models.SET_NULL, null=True
    )
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.date_end


class Staff(models.Model):
    fio = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    birthday = models.DateField()
    salary = models.CharField(max_length=5)

    def __str__(self):
        return self.fio


class Services(models.Model):
    service_name = models.CharField(max_length=150)

    def __str__(self):
        return self.service_name


class KindSport(models.Model):
    staff_id = models.ForeignKey(
        Staff, on_delete=models.SET_NULL, null=True
    )
    service_id = models.ForeignKey(
        Services, on_delete=models.SET_NULL, null=True
    )
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.service_id


class Rooms(models.Model):
    room_name = models.CharField(max_length=150)

    def __str__(self):
        return self.room_name


class Timetable(models.Model):
    timetable_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    service_id = models.ForeignKey(
        Services, on_delete=models.SET_NULL, null=True
    )
    room_id = models.ForeignKey(
        Rooms, on_delete=models.SET_NULL, null=True
    )
    staff_id = models.ForeignKey(
        KindSport, on_delete=models.SET_NULL, null=True
    )
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.timetable_date


class RegistrationVisits(models.Model):
    sellSubscription_id = models.ForeignKey(
        SellSubscriptions, on_delete=models.SET_NULL, null=True
    )
    timetable_id = models.ForeignKey(
        Timetable, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.sellSubscription_id
