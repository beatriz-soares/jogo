
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', admin.site.urls),
    url(r'^jogo/', include('jogo.urls')),
]
