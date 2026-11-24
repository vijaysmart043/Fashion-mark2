"""
URL configuration for luxury e-commerce project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from apps.core.views import health_check

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin-panel/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
)
