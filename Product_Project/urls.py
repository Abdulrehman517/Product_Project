from django.contrib import admin
from django.urls import path, include
from products.api.views import ProductList, ProductDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('accounts/', include('user_app.api.urls')),
    path('api-auth/', include('rest_framework.urls')),


]
