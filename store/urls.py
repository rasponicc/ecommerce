from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),    
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('register/', views.register,name = "register" ),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('update_wishlist_item/', views.updateWishlistItem, name="update_wishlist_item"),
]