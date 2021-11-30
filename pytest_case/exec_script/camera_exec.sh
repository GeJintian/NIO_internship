#!/bin/bash
while read rows
do
        arr=($rows)
        position=${arr[0]}
        img=${arr[1]}
        rf=${arr[2]}
        sshpass -p root scp /home/jenkins/eol_pytest_test/dataset/camera/img/${position}/image/${img} root@10.42.0.21:/nio/parameters/camera/dummy/${position}/image/${position}.bmp
        sshpass -p root scp /home/jenkins/eol_pytest_test/dataset/camera/img/${position}_archive.json root@10.42.0.21:/nio/parameters/camera/dummy/${position}/${position}_archive.json
        sshpass -p root scp /home/jenkins/eol_pytest_test/dataset/camera/img/${position}_archive.txt root@10.42.0.21:/nio/parameters/camera/dummy/${position}/${position}_archive.txt
        sshpass -p root scp /home/jenkins/eol_pytest_test/dataset/camera/ref/${rf} root@10.42.0.21:/nio/uds/transfers/ref_targets_sideview_force.json
        if [ $position = "front_narrow" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 0 -d
EOF
        elif [ $position = "front_wide" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 1 -d
EOF
        elif [ $position = "front_left" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 2 -d
EOF
        elif [ $position = "front_right" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 3 -d
EOF
        elif [ $position = "rear_left" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 4 -d
EOF
        elif [ $position = "rear_right" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 5 -d
EOF
        elif [ $position = "rear_narrow" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 6 -d
EOF
        elif [ $position = "svc_front" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 7 -d
EOF
        elif [ $position = "svc_left" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 8 -d
EOF
        elif [ $position = "front_narrow" ];then
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 9 -d
EOF
        else
        sshpass -p root ssh root@10.42.0.21<<EOF
                eol_util -s 10 -d
EOF
        fi >/dev/null
        sshpass -p root scp root@10.42.0.21:/nio/parameters/camera/${position}/${position}.json /home/jenkins/eol_pytest_test/dataset/camera/result/${position}/${img}.json
        sshpass -p root scp root@10.42.0.21:/var/log/syslog /home/jenkins/eol_pytest_test/.
        python3 read_syslog.py --input-dir /home/jenkins/eol_pytest_test/syslog --output-dir /home/jenkins/eol_pytest_test/dataset/camera/log/${position}/${img}.log
done</home/jenkins/eol_pytest_test/dataset/camera_test_list.txt
cd ../test_case/camera_test
python3 main.py config.txt