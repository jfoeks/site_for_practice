from django.urls import path
from .views import products, basket_add,basket_remove,basket_add_up,basket_add_down

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('baskets/add_up/<int:basket_id>/', basket_add_up, name='basket_add_up'),
    path('baskets/add_down/<int:basket_id>/', basket_add_down, name='basket_add_down')
]