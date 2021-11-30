pcd=$1
rf=$2
sshpass -p root scp /home/jenkins/eol_pytest_test/dataset/lidar/pcd/${pcd} root@10.42.0.21:/nio/parameters/lidar/dummy/lidar_front.pcd
sshpass -p root scp /home/jenkins/eol_pytest_test/dataset/lidar/ref/${rf} root@10.42.0.21:/nio/uds/transfers/ref_targets_lidar_force.json
sshpass -p root ssh root@10.42.0.21 >/dev/null <<EOF
        eol_util -s 11 -d
EOF
sshpass -p root scp root@10.42.0.21:/nio/parameters/lidar/lidar_front.json /home/jenkins/eol_pytest_test/dataset/lidar/result/${pcd}.json
sshpass -p root scp root@10.42.0.21:/var/log/syslog /home/jenkins/eol_pytest_test/.
python3 read_syslog.py --input-dir /home/jenkins/eol_pytest_test/syslog --output-dir /home/jenkins/eol_pytest_test/dataset/lidar/log/${pcd}.log
