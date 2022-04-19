from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('chapters/', include('Chapters.urls')),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
    ), name='documentation'),
]
