import sys, getopt
def usage():
    print('usages: python msu2rap -i <msu_file> -t <trans_file> -o <rap_file> \n')
opts, args = getopt.getopt(sys.argv[1:], "ht:i:o:")

trans_file = ""
msu_file = ""
rap_file = ""

for op, value in opts:
    if op == '-i':
        msu_file = value
    elif op == '-o':
        rap_file = value
    elif op == '-t':
        trans_file = value
    elif op == '-h':
        usage()
        exit(0)
def run():
    relation={}
    for i in open(trans_file):
        rap=str(i.split()[0])
        msu=str(i.split()[1])
        if msu!="None":
            if "," in msu:
                for a in msu.split(","):
                    relation[a[0:-2]] = rap
            else:
                relation[msu[0:-2]] = rap

    with open(rap_file, "w") as f:
        for j in open(msu_file, 'r'):
            id=j.strip()
            if id in relation.keys():
                line = id + '\t' + relation[id] + '\n'
                f.write(line)
            else:
                line = id + '\tNone\n'
                f.write(line)
if __name__ == '__main__':
    run()
