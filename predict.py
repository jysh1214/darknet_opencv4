import glob
import subprocess
import time

if __name__ == '__main__':
    for filename in glob.glob("./QA/*"):
        command = ("./darknet detector test cfg/lesion.data cfg/lesion.cfg lesion.weights {0}" .format(filename))
        subprocess.call(command, shell=True)
