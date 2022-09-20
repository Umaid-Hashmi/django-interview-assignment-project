from django.urls import include, path
from rest_framework.authtoken import views
from pustakaalay_app import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)
from django.contrib import admin

urlpatterns = [
    path('', include('pustakaalay_app.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
