from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('hizb/', include('Hizb.urls')),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
    ), name='documentation'),
]
