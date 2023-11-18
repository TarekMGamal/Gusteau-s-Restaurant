from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, CategoryViewSet

menu_item_router = DefaultRouter()
category_router = DefaultRouter()

menu_item_router.register(r'', MenuItemViewSet, basename='menu-item')
category_router.register(r'', CategoryViewSet, basename='category')

urlpatterns = [
    path('menu-items/', include(menu_item_router.urls)),
    path('categories/', include(category_router.urls)),
]
