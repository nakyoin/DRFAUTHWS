from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('prod/', views.ProdApi.as_view()),
    path('prod/<int:pk>/', views.ProdDetail.as_view()),
    path('cart/', views.CartApi.as_view()),
    path('cart/<int:pk>', views.CartDetail.as_view()),
    path('order/', views.OrderApi.as_view()),
    path('order/<int>', views.OrderDetail.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]