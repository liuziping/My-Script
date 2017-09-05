# _*_ coding: utf-8 _*_
from django.conf.urls import url 
from server import idc,servers,product

urlpatterns = [ 
    url('^idc_add/$',idc.AddIdcView.as_view(), name='idc_add'),
    url('^idc_list/$',idc.IdcListView.as_view(), name='idc_list'),

    url('^server_add/$',servers.AddServerView.as_view(), name='server_add'),
    url('^server_list/$',servers.ServerListView.as_view(), name='server_list'),
    url('^modify_status/$',servers.ModifyServerStatusView.as_view(), name='modify_status'),
    url('^modify_product/$',servers.ModifyProductView.as_view(), name='modify_product'),
    url('^get_server/$',servers.ServerGetView.as_view(), name='get_server'),
    
    url('^product_manage/$',product.ProductManageView.as_view(), name='product_manage'),
    url('^product_add/$',product.ProductAddView.as_view(), name='product_add'),
    url('^product_get/$',product.ProductsGetView.as_view(), name='product_get'),
    url('^product_manage_get/$',product.ProductManageGetView.as_view(), name='product_manage_get'),
]
