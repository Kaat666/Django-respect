from django.urls import path
from category import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("category/<int:category_id>/", views.CategoriesProduct.as_view()),
    path("category/", views.CategoryList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
