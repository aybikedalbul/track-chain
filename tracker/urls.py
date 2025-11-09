from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("products/new/", views.ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("products/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path(
        "products/<int:product_pk>/events/new/",
        views.ProductEventCreateView.as_view(),
        name="event_create",
    ),
    path("events/<int:pk>/edit/", views.ProductEventUpdateView.as_view(), name="event_update"),
    path("events/<int:pk>/delete/", views.ProductEventDeleteView.as_view(), name="event_delete"),
]
