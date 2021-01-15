from django.db import models


class CarPlan(models.Model):
    plan_name = models.CharField(max_length=20)
    warranty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.plan_name


class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    car_plan = models.ForeignKey(
        CarPlan, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.car_brand


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Manufacturers(models.Model):
    manufacturer_name = models.CharField(max_length=150)

    def __str__(self):
        return self.manufacturer_name


class Providers(models.Model):
    provider_name = models.CharField(max_length=150)

    def __str__(self):
        return self.provider_name


class Supplies(models.Model):
    provider_id = models.ForeignKey(
        Providers, on_delete=models.CASCADE
    )
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%m/%d/%Y")


class Products(models.Model):
    category_id = models.ForeignKey(
        Categories, on_delete=models.CASCADE
    )
    manufacturer_id = models.ForeignKey(
        Manufacturers, on_delete=models.SET_NULL, null=True
    )
    supply_id = models.ForeignKey(
        Supplies, on_delete=models.SET_NULL, null=True
    )
    product_name = models.CharField(max_length=150)
    product_desc = models.CharField(max_length=500)
    product_price = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name


class Customers(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Sellers(models.Model):
    name = models.CharField(max_length=150)
    POSITIONS = (
        (1, 'Position1'),
        (2, 'Position2'),
        (3, 'Position3'),
    )
    position = models.IntegerField(choices=POSITIONS)
    passport = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Accounts(models.Model):
    customer_id = models.ForeignKey(
        Customers, on_delete=models.CASCADE
    )
    seller_id = models.ForeignKey(
        Sellers, on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Products, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    discount = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%m/%d/%Y")
