from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members_app.urls')),
    path('bryan/', include('book_app.urls')), #bryan/books
    path('admin/', admin.site.urls),
]