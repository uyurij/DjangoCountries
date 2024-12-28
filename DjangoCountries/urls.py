from django.urls import path
from Countries import views
#from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('country/<int:country_id>', views.get_country, name='country-detail'),
    path('countries', views.get_countries, name='countries-list'),
    path('url/', views.login, name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

