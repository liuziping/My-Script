# _*_ coding: utf-8 _*_

from django import forms
from dashboard.models import UserProfile
from server.models import Product


class IdcForm(forms.Form):
    name        = forms.CharField(required=True,max_length=20,
                    error_messages={"required":"机房简称不能为空","max_length":"长度必须小于10"})
    idc_name    = forms.CharField(required=True,max_length=100)
    address     = forms.CharField(required=True,max_length=255)
    user        = forms.CharField(required=True,max_length=32)
    user_phone  = forms.CharField(required=True,max_length=20)
    user_email  = forms.EmailField(required=True,max_length=32)


    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name.lower()

class ProductForm(forms.Form):

    name            = forms.CharField(required=True, max_length=32,
                                      error_messages={"required": "业务线名称不能为空", "max_length": "长度必须小于32"})

    module_letter   = forms.CharField(required=True, max_length=10,
                                      error_messages={"required": "业务线简称不能为空", "max_length": "长度必须小于10"})
    pid       = forms.CharField(required=True)
    op_interface    = forms.MultipleChoiceField(choices=((obj.username, obj.email) for obj in UserProfile.objects.all()))
    dev_interface   = forms.MultipleChoiceField(choices=((obj.username, obj.email) for obj in UserProfile.objects.all()))

    def clean_module_letter(self):
        # 自定义字段验证  clean_字段名称
        # 获取name
        module_letter = self.cleaned_data.get("module_letter")
        # 处理转换为小写
        module_letter.strip().lower()
        return module_letter

    def clean_pid(self):
        # 上级业务线：
        # 顶级业务线为 0
        # 非顶级业务线需要验证上级业务线是否存在
        
        pid = self.cleaned_data.get("pid")
        print pid
        if pid.isdigit():
            if int(pid) != 0:
                try:
                    Product.objects.get(pk=pid)
                except:
                    raise forms.ValidationError('上级业务线不存在')
        else:
            raise forms.ValidationError('请选择正确的上级业务线')
        return pid
 


    def clean_op_interface(self):
        op_interface = self.cleaned_data.get("op_interface")
        return ",".join(op_interface)

    def clean_dev_interface(self):
        dev_interface = self.cleaned_data.get("dev_interface")
        return ",".join(dev_interface)

    def clean(self):
        # 要先调用父类的方法
        super(ProductForm, self).clean()



