from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('offer-mng/', include('offer_mng.urls')),
    path('offer/', include('offer.urls')),
    path('issues/', include('issues.urls')),
    path('register/', include('offer.urls_register')), 
]