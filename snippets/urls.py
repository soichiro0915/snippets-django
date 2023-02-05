from django.contrib import admin
from django.urls import path, include
from snippetsapp.views import top

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippetsapp.urls')),
    path("admin/", admin.site.urls),
]
