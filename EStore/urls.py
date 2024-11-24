from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product import views as product_views  # Import the home view from product app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_views.home, name='home'),  # Use the correct home view
    path('products/', include('product.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
