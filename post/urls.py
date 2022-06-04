from django.urls import path
from .views import home, new_entry, detail, post_delete

urlpatterns = [
    path('', home, name='home'),
    path('new_entry/', new_entry, name='new_entry'), 
    path('detail/<slug:slug>/', detail, name='detail'), 
    path('post_delete/<slug:slug>/', post_delete, name='post_delete'), 
    # path('change_like/<slug:slug>/', change_like, name='change_like'), 


]