from django.urls import path
from mspayment import views

urlpatterns = [
    path("checkout/<uuid:pk>/", views.CreateCkeckoutView.as_view(), name="checkout"),
    path(
        "checkout-simple/<uuid:pk>/",
        views.CreateCheckoutSimpleView.as_view(),
        name="checkout-simple",
    ),
]
