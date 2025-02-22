from rest_framework.routers import DefaultRouter

from media import views

app_name = "media"

router = DefaultRouter()
router.register("imagesUpload", views.ImageUploadViewSet)
router.register("documents", views.DocumentUploadViewSet)
