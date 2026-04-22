from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home_view, name='home'), 
    
    # All Products (Mobiles)
    path('all-phones/', views.phone_list_view, name='phone_list'),
    
    # Detail Page - (Maine iska name 'phone_detail' kar diya hai taaki error hat jaye)
    path('product/<slug:slug>/', views.phone_detail_view, name='phone_detail'),
    
    # Compare
    path('compare/', views.compare_phones, name='compare_phones'),
    
    # SIGNUP
    path('signup/', views.signup_view, name='signup'),

    # --- NAYE CATEGORY URLS (Laptop, TV, Tablet ke liye) ---
    # Jab user Laptop box par click karega toh ye kaam aayenge
    path('laptops/', views.phone_list_view, {'category': 'laptop'}, name='laptop_list'),
    path('tvs/', views.phone_list_view, {'category': 'tv'}, name='tv_list'),
    path('tablets/', views.phone_list_view, {'category': 'tablet'}, name='tablet_list'),
]