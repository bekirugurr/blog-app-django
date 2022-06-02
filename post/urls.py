from django.urls import path
from .views import home, new_entry

urlpatterns = [
    path('', home, name='home'),
    path('new_entry/', new_entry, name='new_entry'), 

]