#!/usr/bin/env python
#encoding: utf8
import subprocess
import os


def jtalk(t):
    path = os.path.dirname(os.path.realpath(__file__)) + \
        '/open_jtalk.wav'
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = [
        '-m', path + 'scripts/tohoku-f01-happy.htsvoice']
    #speed = ['-r', '1.0']
    outwav = ['-ow', path]
    cmd = open_jtalk + mech + htsvoice + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay', '-q', path]
    wr = subprocess.Popen(aplay)


"""
Open-jtalkをPythonで使用するための関数
t - しゃべらせたいテキスト
"""
