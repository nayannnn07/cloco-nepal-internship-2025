from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class BookCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return BookCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get(
            "category_name", instance.category_name
        )
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    details = serializers.CharField(allow_blank=True, required=False)
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )  # Change to related field
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all()
    )  # Change to related field
    category = serializers.PrimaryKeyRelatedField(
        queryset=BookCategory.objects.all()
    )  # Change to related field

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.details = validated_data.get("details", instance.details)
        instance.author = validated_data.get("author", instance.author)
        instance.publisher = validated_data.get("publisher", instance.publisher)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.contact = validated_data.get("contact", instance.contact)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order_date = serializers.DateTimeField()
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_date = validated_data.get("order_date", instance.order_date)
        instance.customer = validated_data.get("customer", instance.customer)
        instance.save()
        return instance


class OrderDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    customer_name = serializers.CharField(max_length=255)
    customer_email = serializers.EmailField()
    customer_address = serializers.CharField(max_length=255)
    customer_contact = serializers.CharField(max_length=10)
    order_status = serializers.ChoiceField(
        choices=OrderStatus.choices, default=OrderStatus.PENDING
    )

    def create(self, validated_data):
        return OrderDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order = validated_data.get("order", instance.order)
        instance.book = validated_data.get("book", instance.book)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.price = validated_data.get("price", instance.price)
        instance.customer_name = validated_data.get(
            "customer_name", instance.customer_name
        )
        instance.customer_email = validated_data.get(
            "customer_email", instance.customer_email
        )
        instance.customer_address = validated_data.get(
            "customer_address", instance.customer_address
        )
        instance.customer_contact = validated_data.get(
            "customer_contact", instance.customer_contact
        )
        instance.order_status = validated_data.get(
            "order_status", instance.order_status
        )
        instance.save()
        return instance


class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    total_amount = serializers.DecimalField(max_digits=7, decimal_places=2)

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.book = validated_data.get("book", instance.book)
        instance.customer = validated_data.get("customer", instance.customer)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.price = validated_data.get("price", instance.price)
        instance.total_amount = validated_data.get(
            "total_amount", instance.total_amount
        )
        instance.save()
        return instance


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    total_amount = serializers.DecimalField(max_digits=7, decimal_places=2)
    payment_method = serializers.ChoiceField(choices=PaymentMethod.choices)

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customer = validated_data.get("customer", instance.customer)
        instance.order = validated_data.get("order", instance.order)
        instance.total_amount = validated_data.get(
            "total_amount", instance.total_amount
        )
        instance.payment_method = validated_data.get(
            "payment_method", instance.payment_method
        )
        instance.save()
        return instance
