for i in 0 1 5
do
    sudo ip link set can$i down
    sudo ip link set can$i up type can bitrate 500000
    sudo ifconfig can$i txqueuelen 10000
done
for i in 2 3 4
do
    sudo ip link set can$i down
    sudo ip link set can$i up type can bitrate 500000 sample-point 0.8 dbitrate 2000000 fd on
    sudo ifconfig can$i txqueuelen 10000
done
cangen can0 -g 500 -I 505 -L 8 -D 0040FFFFFFFFFFFF &