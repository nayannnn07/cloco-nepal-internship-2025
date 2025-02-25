from django.db import models

# AUTHOR TABLE
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# PUBLISHER TABLE
class Publisher(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

# BOOK CATEGORY TABLE
class BookCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

# BOOK TABLE
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# CUSTOMER TABLE
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# USER TABLE
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

# ORDER STATUS ENUM
class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    DELIVERED = 'delivered', 'Delivered'
    CANCELED = 'canceled', 'Canceled'

# PAYMENT METHOD ENUM
class PaymentMethod(models.TextChoices):
    PAID = 'paid', 'Paid'
    UNPAID = 'unpaid', 'Unpaid'

# ORDERS TABLE
class Order(models.Model):
    order_date = models.DateTimeField("order date")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

# ORDER DETAIL TABLE
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_address = models.CharField(max_length=200)
    customer_contact = models.CharField(max_length=10)
    order_status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    def __str__(self):
        return f"Order {self.order.id} - {self.book.title}"

# CART TABLE
class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.customer.name} - {self.book.title}"

# PAYMENT TABLE
class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices)

    def __str__(self):
        return f"Payment {self.id} - {self.customer.name}"
