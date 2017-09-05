#coding:utf-8
from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404,QueryDict
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from urllib import urlencode
from django.core import serializers
import json
import logging

from django.conf import settings
from server.models import Server,Status,Product
from utils.mixin_utils import LoginRequiredMixin 

logger = logging.getLogger('opsweb')

class AddServerView(LoginRequiredMixin,View):
    def post(self,request):
            ret = {'status':0,'errmsg':'ok'}
            data = QueryDict(request.body)
            data = dict(data.items())
            try:
                server = Server(**data)
                server.save()  
            except Exception as e:
                msg = "user {} add server error:{}".format(request.user.username,e.args)
                logger.error(msg)
                ret['status'] = 1
                ret['errmsg']   = msg
            
            return JsonResponse(ret,safe=True)

class ServerListView(LoginRequiredMixin,ListView):
    model = Server
    template_name = "server/server_list.html"
    paginate_by = 10
    before_index = 6
    after_index = 5
   
    def get_queryset(self):
        queryset = super(ServerListView, self).get_queryset()
        queryset = self.get_search_queryset(queryset)
        return queryset
    
    def get_search_queryset(self,queryset):
        hostname = self.request.GET.get('hostname',"").strip().lower()
        queryset = queryset.filter(hostname__contains=hostname)
        inner_ip = self.request.GET.get('inner_ip',"").strip().lower()
        queryset = queryset.filter(inner_ip__contains=inner_ip)
        return queryset 

    def get_uri(self):
        args = self.request.GET.copy()
        if args.has_key('page'):
            args.pop('page')
        return args.urlencode()


    def get_context_data(self, **kwargs):
        context = super(ServerListView, self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        context['products'] = self.get_product()
        context.update(self.request.GET.dict())
        context['uri'] = self.get_uri()
        return context

    def get_product(self):
        ret = {}
        products = Product.objects.filter(pid__exact=0)
        for product in products:
            ret[product.id] = product.name
        return ret

    def get_page_range(self, page_obj):
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        return page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]
    
    def get(self,request,*args, **kwargs):
        return super(ServerListView, self).get(request,*args,**kwargs)

class ModifyServerStatusView(LoginRequiredMixin,TemplateView):
    template_name = "server/modify_server_status.html"

    def get_context_data(self,**kwargs):
        context = super(ModifyServerStatusView,self).get_context_data(**kwargs)
        context['obj'] = get_object_or_404(Server,pk=self.request.GET.get('id',None))
        context['status_obj_list'] = Status.objects.all()
        return context  

    def post(self,request):
        ret = {'code':0,"next_url":reverse("server_list")}
        next_url = request.GET.get('next_url',"")
        if next_url:
            ret['next_url'] = next_url
        obj = get_object_or_404(Server,pk=self.request.GET.get('id',None))
        try:
            obj.status = request.POST.get('status','')
            obj.save()
        except Exception as e:
            ret['status'] = 1
            ret['errmsg'] = e.args

        return render(request,settings.JUMP_PAGE,ret)


class ModifyProductView(LoginRequiredMixin,TemplateView):                                        
    
    template_name = "server/server_modify_product.html"                       
       
    def get_context_data(self, **kwargs):
        context = super(ModifyProductView, self).get_context_data(**kwargs)
        context['server'] = Server.objects.get(pk=self.request.GET.get('id', None))
        context['products'] = Product.objects.all()
        return context
        
    def post(self, request):
        ret = {'code': 0, 'next_url': reverse('server_list')}
        try:
            Server.objects.filter(pk=request.POST.get("id", 0)).update(service_id=request.POST.get("service_id",0),server_purpose=request.POST.get("server_purpose", 0))           
        except Exception as e:
            data['errmsg'] = e.args
            ret['status'] = 1
            logger.error("modify server product error:{}".format(e.args))
        return render(request, settings.JUMP_PAGE, ret)


class ServerGetView(LoginRequiredMixin,View):
    '''
       点击业务线时。显示其包含的主机，外键
    '''
    def get(self, request):
        server_purpose = request.GET.get('server_purpose', None)
        if server_purpose and server_purpose.isdigit():
            queryset = Server.objects.filter(server_purpose_id=server_purpose)
        return HttpResponse(serializers.serialize("json", queryset), content_type="application/json")
