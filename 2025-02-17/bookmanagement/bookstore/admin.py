cd ..
from django.contrib import admin
from .models import Author, Publisher, BookCategory, Book, Customer, User, Order, OrderDetail, Cart, Payment

# Register your models here
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(Payment)
