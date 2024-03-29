from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenVerifyView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('jwt_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt_verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('vid/',include('movie.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
