./wakeup.sh
sshpass -p root scp /home/jenkins/eol_pytest_test/lidar.pcd root@10.42.0.21:/nio/parameters/lidar/dummy/lidar_front.pcd
sshpass -p root ssh root@10.42.0.21 << EOF
    eol_util -s 11 -d
EOF
sleep 10
sshpass -p root scp root@10.42.0.21:/nio/parameters/lidar/lidar_front.json /home/jenkins/eol_pytest_test/
pytest