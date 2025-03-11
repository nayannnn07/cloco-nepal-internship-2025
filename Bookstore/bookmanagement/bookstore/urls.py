from django.urls import path
from .views import *


urlpatterns = [
    # Author API URLs
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Publisher API URLs
    path('publishers/', PublisherListView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),

    # Book Category API URLs
    path('categories/', BookCategoryListView.as_view(), name='book-category-list'),
    path('categories/<int:pk>/', BookCategoryDetailView.as_view(), name='book-category-detail'),

    # Book API URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Customer API URLs
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    # User API URLs
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Order API URLs
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    # Order Detail API URLs
    path('order-details/', OrderDetailListView.as_view(), name='order-detail-list'),
    path('order-details/<int:pk>/', OrderDetailDetailView.as_view(), name='order-detail-detail'),

    # Cart API URLs
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),

    # Payment API URLs
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
