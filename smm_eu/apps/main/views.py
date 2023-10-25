from django.shortcuts import render
from .models import Products, Order
from django.http import Http404, HttpResponseRedirect


def index(request):
    return render(request, 'main/main.html')
##################################################################################################################
######################################INSTAGRAME SECTION##########################################################
##################################################################################################################
def instagramfol(request):
    list_inst_fol = Products.objects.filter(type=1)
    return render(request, 'main/instagramfol.html', {'list_inst_fol': list_inst_fol})

def instagramlike(request):
    list_inst_views = Products.objects.filter(type=2)
    return render(request, 'main/instagramlike.html', {'list_inst_views': list_inst_views})

def instagramautolike(request):
    list_inst_auto_like = Products.objects.filter(type=3)
    return render(request, 'main/instagramautolike.html', {'list_inst_auto_like': list_inst_auto_like})

def instagramviews(request):
    list_inst_like = Products.objects.filter(type=4)
    return render(request, 'main/instagramlike.html', {'list_inst_like': list_inst_like})

def instagramfolbuy(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
    except:
        raise Http404('Not Found!')
    return render(request, 'main/instagramfolbuy.html', {'order_by_id_fol': order_by_id_fol})

def instagramlikebuy(request, price_id):
    try:
        order_by_id_like = Products.objects.get(id=price_id)
    except:
        raise Http404('Not Found!')
    return render(request, 'main/instagramlikebuy.html', {'order_by_id_like': order_by_id_like})
##################################################################################################################
##################################################################################################################

def tiktokfol(request):
    list_tik_tok_fol = Products.objects.filter(type=6)
    return render(request, 'main/tiktokfol.html', {'list_tik_tok_fol': list_tik_tok_fol})

def tiktoklike(request):
    list_tik_tok_like = Products.objects.filter(type=5)
    return render(request, 'main/tiktoklike.html', {'list_tik_tok_like': list_tik_tok_like})

def tiktokviews(request):

    list_tik_tok_views = Products.objects.filter(type=7)
    return render(request, 'main/tiktokviews.html', {'list_tik_tok_views': list_tik_tok_views})
##################################################################################################################
##########################################TIKTOK BUY VIEWS########################################################
##################################################################################################################
def tiktokfolbuy(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
    except:
        raise Http404('Not Found!')
    return render(request, 'main/tiktokfolbuy.html', {'order_by_id_fol': order_by_id_fol})

def tiktoklikebuy(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
    except:
        raise Http404('Not Found!')
    return render(request, 'main/tiktoklikebuy.html', {'order_by_id_fol': order_by_id_fol})

def tiktokviewsbuy(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
    except:
        raise Http404('Not Found!')
    return render(request, 'main/tiktokviewsbuy.html', {'order_by_id_fol': order_by_id_fol})
##################################################################################################################
##################################################################################################################


def order(request, price_id):
    try:
        order_by_id_fol = Products.objects.get(id=price_id)
        amnt = int(order_by_id_fol.count_field.replace(' ', ''))
        Order.objects.create(amount=amnt, type=order_by_id_fol.type)
        type = order_by_id_fol.type_by_type_id
    except:
        raise Http404('Not Found!')
    return render(request, 'main/order.html', {'order_by_id_fol': order_by_id_fol, 'type': type})




