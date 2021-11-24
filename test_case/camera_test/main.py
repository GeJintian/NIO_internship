import pytest
import argparse
parser = argparse.ArgumentParser(description='Lidar callibration test')
parser.add_argument('config_file', metavar='DIR',
                    help='path to config_file')
# parser.add_argument('--thresh', type=str,default="0.01",
#                     help='threshold of lidar test (Default: 0.01)')

def check_error(input_dir,position):
    f=open('/home/jenkins/eol_pytest_test/dataset/camera/log/'+position+'/'+input_dir+'.log','r')
    line=f.readline()[:-1]
    build_time=None
    git_branch=None
    git_hash=None
    while line:
        find = line.split(' ')
        #print(find)
        if "hash" in find:
            git_hash=line.split(']')[-2].split('[')[-1]
        if "branch" in find[-1]:
            git_branch=line.split(']')[-2].split('[')[-1]
        if "build" in find:
            build_time=line.split(']')[-2].split('[')[-1]
        if "calibration..." in find:
            break
        line = f.readline()[:-1]
    print("project building time:",build_time)
    print("project branch:",git_branch)
    print("project git hash:",git_hash)
    is_error = False
    while line:
        if "[ERROR]" in line:
            is_error = True
            print(line)
        line = f.readline()[:-1]
    return is_error

def main():
    args = parser.parse_args()
    #Read config file
    f = open(args.config_file,'r')
    line=f.readline()[:-1]
    config={}
    while line:
        line=line.split(' ')
        config[line[0]] = line[1]
        line=f.readline()[:-1]
    f.close()
    args.data_dir = config['data_dir']
    args.thresh=config['thresh']
    f=open('/home/jenkins/eol_pytest_test/dataset/'+args.data_dir,'r')
    line = f.readline()
    count_total=0
    count_success=0
    while line:
        count_total+=1
        line = line.split(' ')
        img=line[1]
        position=line[0]
        print("====================Checking syslog====================")
        print("Test sample:",img)
        is_error=check_error(img,position)
        if is_error is True:
            line = f.readline()
            print("Error detected, skip test")
            continue
        else:
            print("No error detected, continue test")
            rect=pytest.main(["--position",position,"--tester", img,"--thresh",args.thresh,"-q"])
            if rect == pytest.ExitCode.TESTS_FAILED:
                count_success += 1
            line = f.readline()
    f.close()
    print(count_total,"samples for camera test.")
    print(count_success,"samples pass.")

if __name__=="__main__":
    main()