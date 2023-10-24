from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy-instagram-followers/', views.instagramfol, name='instagramfol'),
    path('buy/instagram-followers/<int:price_id>', views.instagramfolbuy, name='instagramfolbuy'),
    path('buy/order/<int:price_id>', views.order, name='order')
]