from collections import deque
import argparse

parser = argparse.ArgumentParser(description='Read syslog')
parser.add_argument('--input-dir', metavar='DIR', default='/home/jenkins/eol_pytest_test/syslog',
                    help='path to input syslog')
parser.add_argument('--output-dir', metavar='DIR',
                    help='path to input syslog')

def main():
    args = parser.parse_args()
    file=args.input_dir
    error_code=[]
    keep=deque()
    lines=deque(open(file,encoding="latin"))
    line=lines.pop()[:-1]
    #Find end
    while line:
        find = line.split(' ')
        #print(find)
        if "finished!" in find:
            break
        line=lines.pop()[:-1]
    keep.append(line)
    line = lines.pop()[:-1]
    #Find head
    while line:
        find = line.split(' ')
        keep.append(line)
        # if "error_code:" in find:
        #     error_code.append(line)
        print(line)
        if "Initialize..." in find:
            break
        line = lines.pop()[:-1]
    # line = lines.pop()[:-1]
    # git_branch=1
    # git_hash=2
    # build_time=3
    # while line:
    #     find = line.split(' ')
    #     #print(find)
    #     if "hash" in find:
    #         git_hash=line.split(']')[-2].split('[')[-1]
    #     if "branch" in find[-1]:
    #         git_branch=line.split(']')[-2].split('[')[-1]
    #     if "build" in find:
    #         build_time=line.split(']')[-2].split('[')[-1]
    #     if "Initialize..." in find:
    #         break
    #     line = lines.pop()[:-1]
    # print("beginning:",keep.pop()[:-1])
    # print("end:",keep.popleft()[:-1])
    # print(error_code)
    # print("project building time:",build_time)
    # print("project branch:",git_branch)
    # print("project git hash:",git_hash)
    # print("==========content==========")
    f=open(args.output_dir,'w')
    while len(keep)>0:
        f.write(keep.pop()+'\n')
    f.close()

if __name__=="__main__":

    main()