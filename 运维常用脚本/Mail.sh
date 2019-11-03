#!/bin/sh
ip=xx 	#检测的服务ip地址
DATE=`date +%Y-%m-%d/%H:%M:%S`
mail=xx 	#发送人的地址
mailpass=xx		#发送人邮箱授权密码	
to_user=xx		#接收者邮箱
while [ 1 ]
do
        Losspak=`ping -c10 ${ip} 2>/dev/null |grep 'received'|awk -F 'received, |%' '{print $2}'`
        NullLosspak=`echo ${Losspak}|sed 's/[0-9]//g'`
        if [ -z ${NullLosspak} ] 2>/dev/null
        then
                if [ ${Losspak} -ge 40 ]
                then
                        python /root/mail.py ${mail} ${mailpass} ${to_user} "${ip}服务器宕机在时间为${DATE}"
                        exit 0
                fi
        else
                echo 'Tacket is No Runing...'
                exit 0
        fi
        sleep 30

done