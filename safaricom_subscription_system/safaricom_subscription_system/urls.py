from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('code', include('subscription_app.urls')),
    path('subscription/', include('subscription_app.urls')),
    path('admin/', admin.site.urls),
]
