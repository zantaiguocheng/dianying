import os
import time

while True:
    time.sleep(15*60)
    os.chdir('e:/pythonwj/python/pachong/proxylist')
    # git fetch --all 从远端拉取最新文件
    # git reset --hard origin/master 将hard更新为远端文件
    os.system('git fetch --all & git reset --hard origin/master')
