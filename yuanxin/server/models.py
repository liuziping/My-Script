# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from dashboard.models import UserProfile

# Create your models here.

class Idc(models.Model):
    name = models.CharField("IDC字母简称",max_length=10,unique=True)
    idc_name = models.CharField("IDC中文名",max_length=100,unique=True)
    address = models.CharField("IDCd地址",max_length=100)
    user = models.CharField("IDC联系人",max_length=32)
    user_phone = models.CharField("联系人电话",max_length=20)
    user_email = models.EmailField("联系人邮件",max_length=32)

    class Meta:
        db_table = "idc"

   
class Status(models.Model):
    name = models.CharField("状态名",max_length=10,unique=True)
    
    class Meta:
        db_table = "status"

class Product(models.Model):
    name =    models.CharField("业务线名称",max_length=32)
    #pid =    models.ForeignKey("self",null=True,verbose_name="上级业务线")
    pid             = models.IntegerField("上级业务线", db_index=True)
    module_letter =    models.CharField("字母简称",max_length=10)
    op_interface =    models.CharField("运维对接人：username1,username2",max_length=255)
    dev_interface =    models.CharField("业务对接人：username1,username2",max_length=255)


    def __str__(self):
        return "{}".format(self.module_letter)

    class Meta:
        db_table = "product"
    
class Server(models.Model):
    supplier        = models.IntegerField(null=True)
    manufacturers   = models.CharField(max_length=50, null=True)
    manufacture_date= models.DateField(null=True)
    server_type     = models.CharField(max_length=20, null=True)
    sn              = models.CharField(max_length=60, db_index=True, null=True)
    idc             = models.ForeignKey(Idc, null=True)
    os              = models.CharField(max_length=50, null=True)
    hostname        = models.CharField(max_length=50, db_index=True, null=True)
    inner_ip        = models.CharField(max_length=32, null=True, unique=True)
    mac_address     = models.CharField(max_length=50, null=True)
    ip_info         = models.CharField(max_length=255, null=True)
    server_cpu      = models.CharField(max_length=250, null=True)
    server_disk     = models.CharField(max_length=100, null=True)
    server_mem      = models.CharField(max_length=100, null=True)
    status          = models.CharField(max_length=100,db_index=True, null=True)
    remark          = models.TextField(null=True)
    service_id      = models.IntegerField(db_index=True, null=True)
    server_purpose  = models.ForeignKey(Product,null=True)
    check_update_time = models.DateTimeField(null=True)
    vm_status       = models.IntegerField(db_index=True, null=True)
    uuid            = models.CharField(max_length=100, db_index=True,null=True)


    def __str__(self):
        return "{} {}".format(self.hostname, self.inner_ip)

    class Meta:
        db_table = "server"

