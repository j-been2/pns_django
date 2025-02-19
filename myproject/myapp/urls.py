from django.urls import path
from .views import *

urlpatterns = [
    path('', pns, name='pns'),
    path('admin_page/', admin_page, name='admin_page'),
    path('add/<str:model_type>/', add_item, name='add_item'),
    path('edit', edit, name='edit'),
    path('delete', delete, name='delete'),
    
]