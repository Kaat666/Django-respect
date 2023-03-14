from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("product/", views.ProductList.as_view()),
    path("product/<int:pk>/", views.ProductDetail.as_view()),
    path("cart/", views.CartList.as_view()),
    path("cart/<int:pk>/", views.CartDetail.as_view()),
    path("order/", views.OrderList.as_view()),
    path("order/<int:products_id>/", views.OrderDetail.as_view()),
    path("category/<int:category_id>/", views.CategoriesProduct.as_view()),
    path("category/", views.CategoryList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
