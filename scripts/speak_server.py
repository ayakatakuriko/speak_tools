#!/usr/bin/env python
#encoding: utf8
import subprocess
import rospy
from speak_tools.srv import *
import jtalk


def speaker(req):
    jtalk(req.text)
    resp.success = True
    return resp


def speaker_server():
    rospy.init_node('speaker_server')
    srv = rospy.Service("speak_text", SpeakedText, speaker)
    print "Ready to speak text."
    rospy.spin()


if __name__ == '__main__':
    speaker_server()
