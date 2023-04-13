"""sysmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from contracts import views

import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('welcome/', views.welcome, name='home'),
    path('contracts/', views.contract_list, name='contract-list'),
    path('contract/<int:id>', views.contract_detail, name='contract-detail'),
    path('contract/<int:id>/update', views.contract_update, name='contract-update'),
    path('contract/<int:id>/disable', views.contract_disable, name='contract-disable'),
    path('contract/<int:id>/print', views.contract_print, name='contract-print'),
    path('contract/add', views.contract_create, name='contract-create'),
    path('contract/<int:id>/amount', views.contract_amount, name='contract-add-amount'),
    path('contract/<int:id1>/<int:id2>/upd-amount', views.contract_upd_amount, name='contract-upd-amount'),
    path('contract/<int:id>/finance', views.contract_finance, name='contract-add-finance'),
    path('contract/<int:id1>/<int:id2>upd-finance', views.contract_upd_finance, name='contract-upd-finance'),
    path('contract/<int:id>/holder', views.contract_holder, name='contract-add-holder'),
    path('contract/<int:id>/commission', views.contract_commission, name='contract-add-commission'),
]
