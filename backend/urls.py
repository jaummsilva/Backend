from pjgplantas.views import  ChangePasswordView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from pjgplantas.views import (
    BoletoViewSet,
    CartaoViewSet,
    ComentarioViewSet,
    PixViewSet,
    PlantaViewSet,
    RegistrationViewSet,
    MyTokenObtainPairView,
    CompraViewSet,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
from media.router import router as media_router
from django.conf import settings
from django.conf.urls.static import static

path("api/media/", include(media_router.urls)),


router = DefaultRouter()
router.register(r"plantas", PlantaViewSet)
router.register(r"boletos", BoletoViewSet)
router.register(r"cartaos", CartaoViewSet)
router.register(r"pixs", PixViewSet)
router.register(r"comentarios", ComentarioViewSet)
router.register(r"auth", RegistrationViewSet)
router.register(r"compras", CompraViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]

urlpatterns += static(settings.MEDIA_ENDPOINT,
                      document_root=settings.MEDIA_ROOT)
