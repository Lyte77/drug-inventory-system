from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view,name='home'),
    path('add-drug/', add_drug,name='add-drug'),
    path('drug/<int:pk>/edit', edit_drug,name='edit-drug'),
    path('drug/<int:pk>/delete', delete_drug,name='delete-drug'),
    path('add-order/', add_order,name='add-order'),
    path('order/<int:pk>/edit', edit_order,name='edit-order'),
    # path('signup/', signup, name='signup'),


]
