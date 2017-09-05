#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,QueryDict,Http404
from django.core.urlresolvers import reverse
from django.views.generic import View,TemplateView, ListView, RedirectView, FormView
from django.db.models import Q
from django.contrib.auth.models import Permission,Group
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
import traceback,json,logging
from django.utils.decorators import method_decorator
from  django.contrib.auth.decorators import  permission_required


# 自定义模块导入
from .models import WorkOrder
from dashboard.models import UserMessage
from .forms import WorkOrderApplyForm, WorkOrderResultForm
from django.conf import settings
from utils.mixin_utils import LoginRequiredMixin 

logger = logging.getLogger("opsweb")

class WorkOrderApplyView(LoginRequiredMixin,View):
    def get(self, request):
        forms = WorkOrderApplyForm()
        return render(request, 'order/work-order-apply.html', {'forms': forms})

    def post(self, request):
        forms = WorkOrderApplyForm(request.POST)
        if forms.is_valid():
            type = request.POST.get('type', '') 
            title = request.POST.get('title', '') 
            order_contents = request.POST.get('order_contents', '') 
            assign_to = request.POST.get('assign_to')

            work_order = WorkOrder()
            work_order.type = int(type)
            work_order.title = title
            work_order.order_contents = order_contents
            work_order.assign_to_id = int(assign_to)
            work_order.applicant = request.user
            work_order.status = 0 
            work_order.save()

            # 给指派的人发消息
            user_message = UserMessage()
            user_message.user = work_order.assign_to_id
            user_message.message = "您有新的工单，请及时处理！ 工单标题：{}".format(work_order.title)
            user_message.save()

            # 给指派的人发邮件
            send_mail(work_order.title, 
                        work_order.order_contents,
                        settings.EMAIL_FROM,
                        ['787696331@qq.com'],
                        fail_silently=False,)
            return HttpResponseRedirect(reverse('work_order:list'))

        else:
            return render(request, 'order/work-order-apply.html', {'forms': forms, 'errmsg': '工单填写格式出错！'})

class WorkOrderListView(LoginRequiredMixin,ListView):
    '''
        未处理工地列表展示
    '''
    @method_decorator(permission_required('code_release.deal_deploy',login_url='/'))
    def get(self, request):

        # 只显示状态小于2，即，申请和处理中的工单
        work_order_lists = WorkOrder.objects.filter(status__lt=2)

        # 如果不是sa组的用户只显示自己申请的工单，别人看不到你申请的工单，管理员可以看到所有工单
        if 'sa' not in [group.name for group in request.user.groups.all()]:
            work_order_lists = work_order_lists.filter(applicant=request.user)

        search_keywords = request.GET.get('search_keywords')
        if search_keywords:
            work_order_lists.filter(Q(title__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(work_order_lists, 10, request=request)
        work_orders = p.page(page)
        return render(request, 'order/work-order-list.html', {'page_obj': work_orders, 'p': p})

    def delete(self, request):
        try:
            data = QueryDict(request.body)
            work_order_id = data.get('work_order_id', '')
            WorkOrder.objects.filter(id=work_order_id).delete()
            ret = {'code': 0, 'result': '取消工单成功！'}
        except:
            ret = {'code': 1, 'errmsg': '取消工单失败！'}
            logger.error("delete order  error: %s" % traceback.format_exc())
            
        return JsonResponse(ret,safe=True)

class WorkOrderDetailView(LoginRequiredMixin,View):
    """
    工单详情页，包括处理结果表单的填写
    """
    def get(self, request):
        work_order_id = request.GET.get('order_id', 0)
        work_order = WorkOrder.objects.get(id=int(work_order_id))
        return render(request, 'order/work-order-detail.html', {'work_order': work_order})

    def post(self, request):
        work_order_id = request.POST.get('work_order_id', 0)
        work_order = WorkOrder.objects.get(id=int(work_order_id))
        if work_order.status == 0:
            work_order.status = 1
            work_order.save()
            return render(request, 'order/work-order-detail.html', {'work_order': work_order,
                                                                    'msg': '您已经接受工单！'})
        if work_order.status == 1:
            forms = WorkOrderResultForm(request.POST)
            if forms.is_valid():
                result_desc = request.POST.get('result_desc', '')
                work_order.result_desc = result_desc
                work_order.status = 2
                work_order.save()
                return HttpResponseRedirect(reverse('work_order:list'))
            else:
                return render(request, 'order/work-order-detail.html', {'work_order': work_order,
                                                                        'errmsg': '必须填写处理结果！'})
class WorkOrderHistoryView(LoginRequiredMixin,View):

    '''
         历史工单查询
    '''

    def get(self, request):
        work_order_lists = WorkOrder.objects.filter(status=2)

        # 如果不是sa组的用户只显示自己申请的工单，别人看不到你申请的工单，管理员可以看到所有工单
        if 'sa' not in [group.name for group in request.user.groups.all()]:
            work_order_lists = work_order_lists.filter(applicant=request.user)

        search_keywords = request.GET.get('search_keywords', '')
        if search_keywords:
            work_order_lists = work_order_lists.filter(Q(title__icontains=search_keywords)|
                                                       Q(order_contents__icontains=search_keywords)|
                                                       Q(result_desc__icontains=search_keywords))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        
        p = Paginator(work_order_lists, 10, request=request)
        work_orders = p.page(page)

        return render(request, 'order/work-order-history.html', {'page_obj': work_orders, 'p': p})


