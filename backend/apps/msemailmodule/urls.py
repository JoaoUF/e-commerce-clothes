from django.urls import path
from msemailmodule import views

urlpatterns = [
    path('template/', views.TemplateList.as_view()),
    path('template/<uuid>/', views.TemplateDetail.as_view())
]