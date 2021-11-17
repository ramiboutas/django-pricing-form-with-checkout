"""config URL Configuration

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

from django.urls import path, include
from .views import pricing_view, get_payment_methods_view, proceed_with_payment_view

urlpatterns = [
    path('', pricing_view ,name='pricing'),
    path('get-payment-methods/', get_payment_methods_view ,name='get-payment-methods'),
    path('proceed-with-payment/', proceed_with_payment_view ,name='proceed-with-payment'),
]
