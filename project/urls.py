from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls', namespace='main_app')),
    path('', include('shop_app.urls', namespace='shop_app')),
]

# настройки админки
admin.site.site_header = 'Moя админка'
admin.site.index_title = 'Данные магазина'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

