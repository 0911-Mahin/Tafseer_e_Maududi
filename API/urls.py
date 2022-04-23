from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('rub/', include('Ruc.urls')),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
    ), name='documentation'),
    path('api-auth/', include('rest_framework.urls'), name='authen'),
]
