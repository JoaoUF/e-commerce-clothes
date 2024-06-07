from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from msauthentication.views import SignUpView, LogoutAllView, LogoutView, LogInView, VefiryEmailView

urlpatterns = [
    path('login/', LogInView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify-email/', VefiryEmailView.as_view(), name='verify_email'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout_all/', LogoutAllView.as_view(), name='logout_all'),
]