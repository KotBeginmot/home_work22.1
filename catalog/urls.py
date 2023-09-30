from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home, contacts


urlpatterns = [
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('category_product/<int:id>/', Category_ProductsListView.as_view(), name='category_product'),
    path('', home, name='home'),
]