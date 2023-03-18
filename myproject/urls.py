"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from polls.views import *

urlpatterns = [
    path('',include('polls.urls')),
    path('admin/', admin.site.urls),
    path('cart/', cart, name = 'cart'),
    path('description/<int:id>/addCart/', addCart, name = 'addCart'),
    path('description/<int:id>/', description, name = 'description'),
    path('cart/remove/<int:id>/', remove, name = 'remove'),
    path('order/', order_view, name = 'order'),
    # path('cart/order/',order,name='order'),
    path('cart/order/<int:id>', order, name = 'order'),
    # path('cart/orderCart/<int:id>', orderCart, name = 'orderCart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
