import os
import time

while True:
    time.sleep(15*60)
    os.chdir('e:/pythonwj/python/pachong/proxylist')
    os.system('dir')
    os.system('git fetch --all & git reset --hard origin/master')
