from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('serve/<path:file_path>/', views.serve_file, name='serve_file'),
    path('', views.landing_page, name="landing_page"),
]
