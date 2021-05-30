from django.urls import path
from .views import (
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    ProdDetailView
)
from .import views

urlpatterns = [
    path('products/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('products/detail/<int:pk>/', ProdDetailView.as_view(), name='detail'),
    path('products/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
