from django.urls import path, include
from mysite.admin_site import admin_site

urlpatterns = [
    path("admin/", admin_site.urls),
    path("funcionarios/", include("funcionarios.urls")),
]