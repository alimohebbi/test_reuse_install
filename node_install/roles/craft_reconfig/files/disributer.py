import os.path


def dist():
    file1 = open('config_sample.csv', 'r')
    lines = file1.readlines()
    header = None
    flag = False
    for i, line in enumerate(lines):
        if i == 0:
            header = line
            continue
        if not os.path.isfile(f'config_sample{(i % 25)+1}.csv'):
            flag = True
        with open(f'config_sample{(i % 25)+1}.csv', 'a+') as f:
            if flag:
                f.write(header)
                flag = False
            f.write(line)


if __name__ == '__main__':
    dist()
