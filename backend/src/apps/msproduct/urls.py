from django.urls import path
from msproduct import views

urlpatterns = [
    path('bill/', views.BillList.as_view()),
    path('bill/<uuid:pk>/', views.BillDetail.as_view()),
    path('color/', views.ColorList.as_view()),
    path('color/<uuid:pk>/', views.ColorDetail.as_view()),
    path('image/', views.ImageList.as_view()),
    path('image/<uuid:pk>/', views.ImageDetail.as_view()),
    path('item/', views.ImageDetail.as_view()),
    path('item/<uuid:pk>/', views.ImageList.as_view()),
    path('price/', views.PriceList.as_view()),
    path('price/<uuid:pk>/', views.PriceDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<uuid:pk>/', views.ProductDetail.as_view()),
    path('product-image/', views.ProductImageList.as_view()),
    path('product-image/<uuid:pk>/', views.ProductImageDetail.as_view()),
    path('size/', views.SizeList.as_view()),
    path('size/<uuid:pk>/', views.SizeDetail.as_view()),
]
