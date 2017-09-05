# coding:utf8
from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404,QueryDict
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core import serializers
from server.models import Product
from dashboard.models import UserProfile

from  server.forms import ProductForm
from utils.mixin_utils import LoginRequiredMixin 
from django.conf import settings

import json
import logging
logger = logging.getLogger('opsweb')


class Ztree(object):
    def __init__(self):
        self.data = self._get_product()

    def _get_product(self):
        return Product.objects.all()

    def _get_one_product(self):
        return [p for p in self.data if p.pid == 0]

    def _get_second_product(self, pid):
        return [p for p in self.data if p.pid == pid]
    
    def get(self):
        ret = []
        for one_obj in self._get_one_product():                            # 遍历顶级产品线
            tmp = {}
            tmp['pid'] = 0
            tmp['id'] = one_obj.id
            tmp['name'] = one_obj.name
            tmp['children'] = []
            for child in self._get_second_product(one_obj.id):             # 遍历二级产品线
                childrens = {"pid":one_obj.id, "name":child.name, "id":child.id}
                tmp['children'].append(childrens) 
            ret.append(tmp)
        return ret




class ProductAddView(LoginRequiredMixin,TemplateView):
    template_name = "server/product_add.html"

    def get_context_data(self,**kwargs):
        context = super(ProductAddView,self).get_context_data(**kwargs)
        context['user_object_list'] = UserProfile.objects.all()
        context['products'] = Product.objects.filter(pid__exact=0)
        return  context


    def post(self,request):
        ret = {"code":0,'next_url':reverse("product_manage")}

        form = ProductForm(request.POST)
        if form.is_valid():
            try :
                product = Product(**form.cleaned_data)
                product.save()

            except  Exception as e:
                msg = "用户{} 业务线出错：{}".format(request.user.username,e.args)
                logger.error(msg)
                ret['code'] = 1
                ret['errmsg'] = msg

        else:
            msg = "用户{} 添加业务线验证失败:{}".format(request.user.username,form.errors)
            logger.error(msg)

            ret['code'] = 1
            ret['errmsg'] = msg


        return render(request,settings.JUMP_PAGE,ret)
 

class ProductManageView(LoginRequiredMixin,TemplateView):
    template_name = "server/product_manage.html"

    '''
        展示业务线信息
    '''
    def get_context_data(self, **kwargs):
        context = super(ProductManageView, self).get_context_data(**kwargs)
        context['ztree'] = json.dumps(Ztree().get())
        # print context['ztree']
        return context

    '''
        更新业务线信息，主要更改业务线名，简称，op dev四项
    '''
    def post(self, request):
        ret = {"status": 0}
        id = request.POST.get("id"),
        data = {
            "name": request.POST.get("name", ''),
            "module_letter": request.POST.get("module_letter", ""),
            "op_interface": ",".join(request.POST.getlist("op_interface[]", [])),
            "dev_interface": ",".join(request.POST.getlist("dev_interface[]", [])),
        }
        try:
            Product.objects.filter(pk=id[0]).update(**data)
        except Exception as e:
            ret['status'] = 1
            ret['errmsg'] = e.args
        return JsonResponse(ret, safe=False)

class ProductManageGetView(LoginRequiredMixin,View):
    """
        通过id,为业务线显示和更新获取信息，渲染表单
    """

    def get(self, request):
        id = request.GET.get("id", 0) 
        ret = {"status": 0, "errmsg": ""}
        try:
            product = Product.objects.get(pk=id)
            data = product.__dict__
            if data['pid'] == 0:
               data['pid'] = "顶级"
            else:
                    p_product = Product.objects.get(pk=data['pid'])
                    data['pid'] = p_product.name
            del data['_state']
            ret['data'] = data

        except Product.DoesNotExist as e:
            ret['status'] = 1
            ret['errmsg'] = e.args
        return HttpResponse(json.dumps(ret), content_type="application/json")


class ProductsGetView(LoginRequiredMixin,View):
    """
        当一级业务线被选中触发事件，查询二级product信息
    """

    def get(self, request):
        pid = request.GET.get("pid", 0)
        products = Product.objects.filter(pid__exact=pid)
        return HttpResponse(serializers.serialize("json", products), content_type="application/json")



