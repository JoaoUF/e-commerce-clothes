from django.urls import path
from msproduct import views

urlpatterns = [
    path('bill/', views.BillDetail.as_view()),
    path('bill/<uuid:pk>/', views.BillList.as_view()),
    path('color/', views.ColorDetail.as_view()),
    path('color/<uuid:pk>/', views.ColorList.as_view()),
    path('image/', views.ImageDetail.as_view()),
    path('image/<uuid:pk>/', views.ImageList.as_view()),
    path('item/', views.ImageDetail.as_view()),
    path('item/<uuid:pk>/', views.ItemList.as_view()),
    path('price/', views.PriceDetail.as_view()),
    path('price/<uuid:pk>/', views.PriceList.as_view()),
    path('product/', views.ProductDetail.as_view()),
    path('product/<uuid:pk>/', views.ProductList.as_view()),
    path('product-image/', views.ProductImageDetail.as_view()),
    path('product-image/<uuid:pk>/', views.ProductImageList.as_view()),
    path('size/', views.SizeDetail.as_view()),
    path('size/<uuid:pk>/', views.SizeList.as_view()),
]
