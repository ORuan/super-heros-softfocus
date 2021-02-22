from django.contrib import admin
from django.urls import path, include
from accounts.urls import router as accounts_url
from superheros.urls import router as superhero_url
from combats.urls import router as combat_url
from rest_framework.authtoken import views
from accounts.views import GetUuidToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(accounts_url.urls)),
    path('api/v1/', include(superhero_url.urls)),
    path('api/v1/', include(combat_url.urls)),
    path('api-token-auth/', views.obtain_auth_token ),
    path('get-uuid-token/<str:token>/', GetUuidToken.as_view({'get':'list'}))
]
