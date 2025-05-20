from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # если нужно

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('films.urls')),  # пример, подкорректируй под свой код
    path('films/', include('films.urls')),
    path('', RedirectView.as_view(url='/films/', permanent=True)),
]