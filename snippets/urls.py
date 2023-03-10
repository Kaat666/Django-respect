from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("product/", views.ProductList.as_view()),
    path("product/<int:pk>/", views.ProductList.as_view()),
    path("cart/", views.CartDetail.as_view()),
    path("cart/<int:pk>/", views.CartDetail.as_view()),
    path("categories/", views.CategoryDetail.as_view()),
    path("order/", views.OrderList.as_view()),
    path("order/<int:products_id>/", views.OrderList.as_view()),
    path("category/<int:category_id>/", views.CategoriesProduct.as_view()),
    path("category/", views.CategoriesProduct.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
