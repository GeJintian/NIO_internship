#!/bin/bash
./wakeup.sh >/dev/null
sshpass -p root ssh root@10.42.0.21 >/dev/null <<EOF
        if [ ! -d "/nio/uds/transfers" ];then
                mkdir /nio/uds/transfers
        fi
EOF
for i in $*
do
        ./${i}_exec.sh
done
