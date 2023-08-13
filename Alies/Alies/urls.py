"""
URL configuration for Alies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name="login"),
    path('delete-all/', views.delete_all,name='delete-all'),
    path('get-current/', views.get_current,name='get-current'),
    path('checkout/', views.checkout,name='checkout'),
    path('stocks_update/', views.stocks_update,name='stocks_update'),
    path('remove_from_cart/', views.remove_from_cart,name='remove_from_cart'),
    path('export_data/', views.export_data,name='export_data'),
    path('export_to_csv/', views.export_to_csv,name='export_to_csv'),
    path('update-receipt-status/<str:receipt_id>/', views.update_receipt_status, name='update_receipt_status'),
    path('get-receipt-details/<str:receipt_id>/', views.get_receipt_details,name='get_receipt_details'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('checkout/',views.checkout,name="checkout"),
    path('history/',views.history,name="history"),
    path('myview/<str:id>',views.order,name="myview"),
    path('order/',views.order,name="order"),
    path('inventory/', views.inventory, name="inventory"),
    path('pricebook/',views.pricebook,name="pricebook"),
    path('queue/',views.queue,name="queue"),
]

