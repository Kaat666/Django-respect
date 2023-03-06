from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', views.product_list),
    path('cart/', views.cart_detail),
    path('category/', views.category_list),
    path('order/', views.order_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)
