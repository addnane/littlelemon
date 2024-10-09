#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemsView.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('book/',views.Book.as_view({'get': 'list', 'post': 'create'}),name='book'),
    path('reservations/', views.reservations, name="reservations"),
]

