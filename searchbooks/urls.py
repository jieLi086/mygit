# -*- codeing = utf-8 -*-
# @Time : 2021/3/9 14:14
# @Author : 李杰
# @File : urls.py
# @Software : PyCharm

from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# 进行地址映射

urlpatterns = [
    path('findAll/', views.findAll),
    path('d/', views.delete),
    path('u/', views.update),
    path('login/', views.login),
    path('', views.loginpage),
    path('jiansuo/', views.jiansuo),
    path('help/', views.help),
    # path('pagingquery/',views.paging_query),

]
