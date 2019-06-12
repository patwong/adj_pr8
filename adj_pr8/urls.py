from django.contrib import admin
from django.urls import path, include


app_name = 'apr8'
urlpatterns = [
    path('', include('apr8_web.urls')),
    path('adj_pr8/', include('apr8_web.urls')),
    path('admin/', admin.site.urls),
]
