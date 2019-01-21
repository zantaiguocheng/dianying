import functools
import os
import time
from threading import Thread


def timeout(seconds_before_timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (
                func.__name__, seconds_before_timeout))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(seconds_before_timeout)
            except Exception as e:
                print('error starting thread')
                raise e
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

@timeout(300)
def gitupdata():
    # 更新git库内容
    os.chdir('e:/pythonwj/python/pachong/proxylist')
    # git fetch --all 从远端拉取最新文件
    # git reset --hard origin/master 将hard更新为远端文件
    os.system('git fetch --all & git reset --hard origin/master')
