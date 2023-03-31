from django.urls import path
from cart import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/<int:pk>/", views.CartDetail.as_view()),
]
