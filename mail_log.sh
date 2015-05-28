#!/bin/bash
cd /home/liuziping/
function scp_pf2(){
  content=`cat <<!
    spawn /usr/bin/scp -r  liuziping@pf2:/var/log/syslog-ng/mail/mail.log ./ 
    expect Password:
    send "douban2014\n"
    expect eof
    `
  echo "$content"|expect
  tim=`date +%y%m%d`
  mv mail.log /mfs/log/mail/current/pf2/mail$tim.log
}


function scp_pf4(){
  content=`cat <<!
    spawn /usr/bin/scp -r  liuziping@pf4:/var/log/syslog-ng/mail/mail.log ./ 
    expect Password:
    send "douban2014\n"
    expect eof
    `
  echo "$content"|expect
  tim=`date +%y%m%d`
  mv mail.log /mfs/log/mail/current/pf4/mail$tim.log
}


scp_pf2
sleep 120
scp_pf4
