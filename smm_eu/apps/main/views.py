from django.shortcuts import render
from .models import Products, Order
from django.http import Http404, HttpResponseRedirect


def index(request):
    return render(request, 'main/main.html')


def instagramfol(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/instagramfol.html', {'list_inst_fol': list_inst_fol})


def instagramlike(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/instagramlike.html', {'list_inst_fol': list_inst_fol})


def instagramfolbuy(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
    except:
        raise Http404('Not Found!')
    return render(request, 'main/instagramfolbuy.html', {'order_by_id_fol': order_by_id_fol})


def order(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
        amnt = int(order_by_id_fol.count_field.replace(' ', ''))
        Order.objects.create(amount=amnt, type=order_by_id_fol.type)
        type = order_by_id_fol.type_by_type_id
    except:
        raise Http404('Not Found!')
    return render(request, 'main/order.html', {'order_by_id_fol': order_by_id_fol, 'type': type})


def buy100like(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/buy/buy-100-likes-on-instagram.html', {'list_inst_fol': list_inst_fol})


def buy500like(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/buy/buy-500-likes-on-instagram.html', {'list_inst_fol': list_inst_fol})


def buy1000like(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/buy/buy-1000-likes-on-instagram.html', {'list_inst_fol': list_inst_fol})


def buy2500like(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/buy/buy-2500-likes-on-instagram.html', {'list_inst_fol': list_inst_fol})


def buy5000like(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/buy/buy-5000-likes-on-instagram.html', {'list_inst_fol': list_inst_fol})

