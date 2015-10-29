#!/bin/sh
############################################################
#               提供给nagios的短信接口脚本                 #
#功能：运行脚本能给指定的联系人发送指定的内容              #
#作者：liuziping                                           #
#时间：2015.9.7                                            #
############################################################

#操作不正确时的提醒
filename=`basename $0`     #print the scripte name
usage() {
        echo "Usage:"
        echo "/bin/sh  $filename content contact"
        exit 1
}
if [ $# -ne 2 ];then
        usage
fi
#
content=$1
contact=$2
username="*****"
password="*****"
subid=""
url="http://114.*.*.*:8082/SendMT/SendMessage"  #花钱买的短信接口
#curl -d 把参数传给后面的URL,模拟post提交，必须按照短信接口提供的格式才行
curl -d UserName=$username   -d UserPass=$password -d subid=$subid -d  Mobile=$contact -d Content="$content" $url

#将脚本加可执行权限，拷贝到/usr/local/nagios/libexec/sms.sh  内容 手机号(多个手机号逗号隔开)，测试短信发送成功>，即可应用到nagios中 
