from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy-instagram-followers/', views.instagramfol, name='instagramfol'),
    path('buy-instagram-likes/', views.instagramlike, name='instagramlike'),

    path('buy-100-likes-on-instagram/', views.buy100like, name='buy100likes'),
    path('buy-500-likes-on-instagram/', views.buy500like, name='buy500likes'),
    path('buy-1000-likes-on-instagram/', views.buy1000like, name='buy1000likes'),
    path('buy-2500-likes-on-instagram/', views.buy2500like, name='buy2500likes'),
    path('buy-5000-likes-on-instagram/', views.buy5000like, name='buy5000likes'),
    #path('buy-10000-likes-on-instagram/', views.buy10000like, name='buy10000likes'),
    #path('buy-25000-likes-on-instagram/', views.buy25000like, name='buy25000likes'),
    #path('buy-50000-likes-on-instagram/', views.buy50000like, name='buy50000likes'),

    path('buy/instagram-followers/<int:price_id>', views.instagramfolbuy, name='instagramfolbuy'),
    path('buy/order/<int:price_id>', views.order, name='order')
]