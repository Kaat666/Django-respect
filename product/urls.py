from django.urls import path
from product import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("product/", views.ProductView.as_view()),
    path("product/<int:pk>/", views.ProductDetail.as_view()),
]
