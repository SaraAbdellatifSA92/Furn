from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('about', views.about_page, name='about_page'),
    path('reports', views.reports, name='reports'),
    path('rules', views.rules, name='rules'),
    path('rules2', views.rules2, name='rules2'),
    path('cart2', views.cart2, name='cart2'),
]
