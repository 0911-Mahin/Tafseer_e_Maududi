from django.urls import include, path

urlpatterns = [
    path('chapters/', include('Chapters.urls'))
]
