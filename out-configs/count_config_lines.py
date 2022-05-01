import os

dirr = os.getcwd()

dirr = "/home/yrl/PycharmProjects/synet-py3/out-configs/new_2022-04-28_1"

def count_prefix_num(file):
    assert os.path.exists(file)
    with open(file, 'r') as cfg:
        set_iface_flag = False
        lines = cfg.readlines()
        line_numm = len(lines)
    return line_numm

if os.path.isdir(dirr):
    data = {}
    print(os.listdir(dirr))
    for dirs in os.listdir(dirr):
        # for dir in dirs:
        dir_path = dirr+'/'+dirs+'/configs/'
        if os.path.isdir(dir_path) is False:
            continue
        print(dirs)
        all = 0
        for root1, dirs1, files1 in os.walk(dir_path):
            for file in files1:
                all += count_prefix_num(root1+file)
        print(all)




