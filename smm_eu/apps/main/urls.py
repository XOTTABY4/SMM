from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy-instagram-followers/', views.instagramfol, name='instagramfol'),
    path('buy-instagram-likes/', views.instagramlike, name='instagramlike'),
    path('buy-instagram-views/', views.instagramviews, name='instagramviews'),
    path('buy-instagram-auto-likes/', views.instagramautolike, name='instagramautolike'),


    path('buy/instagram-followers/<int:price_id>', views.instagramfolbuy, name='instagramfolbuy'),
    path('buy/instagram-likes/<int:price_id>', views.instagramlikebuy, name='instagramlikebuy'),
    path('buy/buy-instagram-views/<int:price_id>', views.instagramviewsbuy, name='instagramviewsbuy'),
    path('buy/buy-instagram-auto-likes/<int:price_id>', views.instagramautolikebuy, name='instagramautolikebuy'),

    path('buy-tiktok-followers/', views.tiktokfol, name='tiktokfol'),
    path('buy-tiktok-likes/', views.tiktoklike, name='tiktoklike'),
    path('buy-tiktok-views/', views.tiktokviews, name='tiktokviews'),
    path('buy/tiktok-followers/<int:price_id>', views.tiktokfolbuy, name='tiktokfolbuy'),
    path('buy/tiktok-likes/<int:price_id>', views.tiktoklikebuy, name='tiktoklikebuy'),
    path('buy/tiktok-views/<int:price_id>', views.tiktokviewsbuy, name='tiktokviewsbuy'),
    path('buy/order/<int:price_id>', views.order, name='order')
]