from django.urls import path
from .views import *

urlpatterns = [
    path('', pns, name='pns'),
    path('admin_page/', admin_page, name='admin_page'),
    path('add/<str:model_type>/', add_item, name='add_item'),
    path('edit/<str:model_type>/<int:item_id>/', edit_item, name='edit_item'),
    path('delete/<str:model_type>/<int:item_id>/', delete_item, name='delete_item'),
    
]