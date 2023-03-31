from django.urls import path
from order import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("order/", views.OrderView.as_view()),
    path("order/<int:products_id>/", views.OrderDetail.as_view()),
    path("pvz/", views.PvzView.as_view())
]
