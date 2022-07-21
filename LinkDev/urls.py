from django.contrib import admin
from django.urls import path , include
import debug_toolbar

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('base/', include('base.urls')),
]
