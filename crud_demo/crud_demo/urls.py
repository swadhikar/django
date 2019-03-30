from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_view

urlpatterns = [
    path('', accounts_view.login_redirect, name='login_redirect'),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
