from django.contrib import admin
from django.urls import path
from webapp import views as webapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp_views.index_view, name='index'),
    path('product/<int:pk>', webapp_views.product_view, name='product_view'),
    path('product/add', webapp_views.product_create_view, name='create'),
    path('product/<int:pk>/edit/', webapp_views.product_update_view, name='product_update'),
    path('product/<int:pk>/delete/', webapp_views.product_delete, name='product_delete'),
]
