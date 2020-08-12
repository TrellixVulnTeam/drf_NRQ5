from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('', include('snippets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]