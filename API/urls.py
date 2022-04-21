from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
    ), name='documentation'),
]
