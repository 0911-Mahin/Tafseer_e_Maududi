from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('chapters/', include('Chapters.urls')),
    path('juz/', include('Juz.urls')),
    path('hizb/', include('Hizb.urls')),
    path('rub/', include('Rub.urls')),
    path('verse/', include('Verse.urls')),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
    ), name='documentation'),
    path('api-auth/', include('rest_framework.urls'), name='authen'),
]
