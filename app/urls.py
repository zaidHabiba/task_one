from django.contrib import admin
from django.urls import path

from app.views import FetchURL, FetchShortURL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urls/', FetchURL.as_view(), name="fetch_urls"),
    path('<int:pk>', FetchShortURL.as_view(), name="fetch_url"),
]
