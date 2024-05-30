from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from msauthentication.views import RegisterView, LogoutAllView, LogoutView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout authentication'),
    path('logout_all/', LogoutAllView.as_view(), name='logout all authenticatio'),
]