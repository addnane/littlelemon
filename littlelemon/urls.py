#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import Book,register
from django.contrib.auth import views as auth_views

router=DefaultRouter()
router.register(r'tables', Book )

urlpatterns = [
   path('admin/', admin.site.urls),
   path('restaurant/', include('restaurant.urls')),
   path('resraurant/menu/',include('restaurant.urls')),
   path('restaurant/booking/', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.jwt')),
   path('register/', register, name='register'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('', auth_views.LoginView.as_view(template_name='home.html'), name='home'),




]
