from django.urls import path
from category import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("category/<int:category_id>/", views.CategoriesProduct.as_view()),
    path("category/", views.CategoryView.as_view()),
]
