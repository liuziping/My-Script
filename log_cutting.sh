#!/bin/bash
#############################################################
#               nginx日志切割脚本                           #
#功能：每天凌晨对nginx日志进行切割，并归档，删除30天前日志  #
#版本：version1.0                                           #
#作者：liuziping                                            #
#时间：2015.6.24                                            #
#############################################################
pidfile="/usr/local/openresty/nginx/nginx.pid"
log_path="/data/wwwlogs/wen.miaoshou.com/"
year=`date -d yesterday +%Y`
month=`date -d yesterday +%m`
day=`date -d yesterday +%Y%m%d`
log_dir="$log_path/$year/$month"     #format /data/wwwlogs/wen.miaoshou.com/2015/06 
log_name="wen.miaoshou.com_access"
save_days=30

function cut_log(){
    if [ ! -d $log_dir ];then
        mkdir -p $log_dir
    fi    
    /bin/mv   $log_path/*.log  $log_dir/$log_name$day.log
    /bin/kill -HUP `cat $pidfile`
}

function del_oldlog(){
    find $log_path -mtime +$save_days -exec rm -rf {} \;
}

cut_log
del_oldlog

