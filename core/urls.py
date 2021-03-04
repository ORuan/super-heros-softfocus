from django.contrib import admin
from django.urls import path, include
from accounts.urls import router as accounts_url
from superheros.urls import router as superhero_url
from combats.urls import router as combat_url
from rest_framework.authtoken import views
from accounts.views import GetUuidToken
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(accounts_url.urls)),
    path('api/v1/', include(superhero_url.urls)),
    path('api/v1/', include(combat_url.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
