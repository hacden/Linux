#!/bin/bash
current_date=`date -d "-1 day" "+%Y%m%d"`
split -b 65535000 -d -a 4 /home/alvin/myout.txt /home/alvin/log/log_${current_date}_
cat /dev/null > nohup.out

