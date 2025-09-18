
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', include('games.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
] + debug_toolbar_urls()

admin.site.site_header = 'Site administration'