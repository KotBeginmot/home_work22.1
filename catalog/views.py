from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from catalog.apps import CatalogConfig
from catalog.models import Product, ContactData, Category

app_name = CatalogConfig.name


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


class ContactsCreateView(CreateView):
    model = ContactData
    template_name = 'catalog/contacts.html'
    fields = ('name', 'phone', 'text')
    success_url = reverse_lazy('catalog:contacts')


class ProductsListView(ListView):
    model = Category
    template_name = 'catalog/products.html'


class Category_ProductsListView(ListView):
    model = Product
    template_name = 'catalog/category_product.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('id'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category = Category.objects.get(id=self.kwargs.get('id'))
        context_data['title'] = f" Категория {category.name}"

        return context_data