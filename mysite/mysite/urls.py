from django.contrib import admin
from django.urls import path, include
from usuario.views import home_view  # importa a view da home

urlpatterns = [
    path('', home_view, name='home'),  # raiz do site
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
]
