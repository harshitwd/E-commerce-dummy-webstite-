from django.shortcuts import render
from .models import Products
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator  import Paginator

class IndexView(ListView):
    model = Products;
    template_name = 'shop/index.html'
    context_object_name ='product_objects'

    def result(request):
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            product_objects = product_objects.filter(title_icontains='item_name')
        return product_objects


def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != ''  and item_name is not None:
        product_objects = product_objects.filter(title=item_name)

    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{'product_objects':product_objects})


def detail(request,id):
    product_object= Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

#class Detailview(DetailView):
    model = Products
    template_name = 'shop/detail.html'
    context_object_name = 'product_objects'
    
    