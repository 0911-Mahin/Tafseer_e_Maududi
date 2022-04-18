from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('chapters/', include('Chapters.urls')),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]
