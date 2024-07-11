from django.urls import path
from mspayment import views

urlpatterns = [
    path("checkout/<uuid:pk>/", views.CreateCkeckoutView.as_view(), name="checkout")
]
